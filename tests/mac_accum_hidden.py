import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock
import pytest


def to_signed(val, bits):
    if val & (1 << (bits - 1)):
        return val - (1 << bits)
    return val


@cocotb.test()
async def test_signed_mac_accumulation(dut):
    """
    Verify that the MAC correctly accumulates signed 8-bit operands.
    """

    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    # Apply reset
    dut.rst_n.value = 0
    dut.valid.value = 0
    dut.a.value = 0
    dut.b.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1

    expected_acc = 0

    # Test vector: mix of positive and negative values
    test_vectors = [
        (10, 3),
        (-5, 4),
        (7, -2),
        (-8, -3),
    ]

    for a, b in test_vectors:
        dut.valid.value = 1
        dut.a.value = a & 0xFF
        dut.b.value = b & 0xFF

        await RisingEdge(dut.clk)

        expected_acc += a * b

        dut_acc = to_signed(int(dut.acc.value), 32)

        assert dut_acc == expected_acc, (
            f"Accumulation mismatch: expected {expected_acc}, got {dut_acc}"
        )

    # Disable valid and ensure accumulator holds value
    dut.valid.value = 0
    await RisingEdge(dut.clk)
    dut_acc = to_signed(int(dut.acc.value), 32)
    assert dut_acc == expected_acc


# Γ£à CRITICAL: Pytest wrapper function
def test_mac_accum_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner
    
    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent
    
    sources = [
        proj_path / "sources/mac.v",
    ]
    
    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="mac",
        always=True,
    )
    
    runner.test(hdl_toplevel="mac", test_module="mac_accum_hidden")
