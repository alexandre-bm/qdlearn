import pytest 

def test_pop_empty(cell):
    with pytest.raises(ValueError):
        cell.pop()
        
def test_push_pop(cell):
    cell.push("str")
    cell.pop()
    assert cell.cell == []