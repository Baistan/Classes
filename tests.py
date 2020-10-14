from collections import namedtuple

Task = namedtuple("Task",["user","action","done","id"])
Task.__new__.__defaults__ = (None,None,False,None)

def test_defaults():
    task1 = Task()
    task2 = Task(None,None,False,None)
    assert task1 == task2

def test_fields():
    task = Task("mary","meet with spider-man",True,1)
    assert_task = Task("mary","meet with spider-man",True,1)
    assert task == assert_task

def test_task_asdict():
    task = Task("alina","drink Coffee",True,2)
    task_dict = task._asdict()
    task_check = {
        "user":"alina",
        "action":"drink Coffee",
        "done":True,
        "id":2
    }
    assert task_dict == task_check

def test_id_replace():
    task = Task("student","learn tests",False,3)
    task_before = task._replace(done=True,id=10)
    task_expected = Task("student","learn tests",True,10)
    assert task_before == task_expected

