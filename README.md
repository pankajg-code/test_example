# MAC Bug Fix Problem

This problem tests the ability to fix a multiply-accumulate (MAC) module with signed arithmetic issues.

## Problem Description

The MAC module has a bug where it treats inputs as unsigned instead of signed, causing incorrect accumulation for negative values.

## Branches

- `1_MAC_bug_fix_baseline`: Starting point with broken implementation
- `1_MAC_bug_fix_test`: Test suite for validation
- `1_MAC_bug_fix_golden`: Reference solution with correct signed arithmetic

