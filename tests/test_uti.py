import aiwolf_nlp_common.util as util

def test_read_text_file(text_file_path) -> None:
    with open(text_file_path,"r",encoding="utf-8") as f:
        correct_list =  f.read().splitlines()
    
    check_list = util.read_text_file(text_file_path=text_file_path)

    correct_list.sort()
    check_list.sort()

    assert correct_list == check_list