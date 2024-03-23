from enum import Enum
import re

class BlockTypes(Enum):
    block_type_paragraph="paragraph"
    block_type_heading="heading"
    block_type_code="code"
    block_type_quote="quote"
    block_type_unordered_list="unordered_list"
    block_type_ordered_list="ordered_list"

# https://regex101.com/
def is_Heading(lines):
    rxpr = re.compile(r"^#{1,6} .*$")

    if not lines:
        return False
    for line in lines:
        matches = rxpr.match(line)
        if not matches:
            return False
    return True

def is_Code(lines):
    if not lines:
        return False
    return (lines[0].startswith("\'\'\'") and lines[-1].endswith("\'\'\'"))

def is_Quote(lines):
    rxpr = re.compile(r"^> .*$")

    if not lines:
        return False
    for line in lines:
        matches = rxpr.match(line)
        if not matches:
            return False
    return True

def is_UnorderedList(lines):
    rxpr = re.compile(r"^(\*|-) .*$")

    if not lines:
        return False
    for line in lines:
        matches = rxpr.match(line)
        if not matches:
            print("--- -- -", line)
            return False
    return True

def is_OrderedList(lines):
    if not lines:
        return False
    for line, index in zip(lines,range(1,len(lines)+1)):
        if not line.startswith(f"{index}. "):
            return False
    return True


def block_to_block_type(block):
    lines = block.split('\n')
    if is_Heading(lines):
        return BlockTypes.block_type_heading
    elif is_Code(lines):
        return BlockTypes.block_type_code
    elif is_Quote(lines):
        return BlockTypes.block_type_quote
    elif is_UnorderedList(lines):
        return BlockTypes.block_type_unordered_list
    elif is_OrderedList(lines):
        return BlockTypes.block_type_ordered_list
    else:
        return BlockTypes.block_type_paragraph