import unittest

from block_types import BlockTypes, block_to_block_type

class TestBlockTypes(unittest.TestCase):
    def test_block_type(self):
        param_list = [
             ("t0", BlockTypes.block_type_paragraph),
             ("# h1", BlockTypes.block_type_heading),
             ("## h2", BlockTypes.block_type_heading),
             ("## h2\n## h2", BlockTypes.block_type_heading),
             ("## h2\nh2", BlockTypes.block_type_paragraph),
             ("### h3", BlockTypes.block_type_heading),
             ("#### h4", BlockTypes.block_type_heading),
             ("##### h5", BlockTypes.block_type_heading),
             ("###### h6", BlockTypes.block_type_heading),
             ("####### t7", BlockTypes.block_type_paragraph),
             ("'''c1'''", BlockTypes.block_type_code),
             ("'''c1\nc2'''", BlockTypes.block_type_code),
             ("> q1", BlockTypes.block_type_quote),
             ("> q1\n> q2", BlockTypes.block_type_quote),
             ("> q1\n q2", BlockTypes.block_type_paragraph),
             ("* q1\n* q2", BlockTypes.block_type_unordered_list),
             ("- q1\n- q2", BlockTypes.block_type_unordered_list),
             ("- q1\nq2", BlockTypes.block_type_paragraph),
             ("1. q1\n2. q2", BlockTypes.block_type_ordered_list),
             ("2. q1\n2. q2", BlockTypes.block_type_paragraph),
             ("1. q1\n3. q2", BlockTypes.block_type_paragraph),
             ("1. q1\nq2", BlockTypes.block_type_paragraph),
              ]
        for param_in, expected in param_list:
            with self.subTest(param_in):
                self.assertEqual(block_to_block_type(param_in), expected)

if __name__ == "__main__":
    unittest.main()