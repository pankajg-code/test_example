You are given an RTL implementation of a multiply–accumulate (MAC) module.



The module multiplies two 8-bit inputs and accumulates the result into a 32-bit register

when `valid` is asserted. The accumulator is reset to zero when `rst\_n` is low.



The current implementation produces incorrect results for certain input values.



Your task is to fix the RTL so that the MAC produces correct accumulation results for all

valid input combinations while preserving the existing interface and behavior.



Do not modify the module interface.

Do not add new inputs or outputs.



