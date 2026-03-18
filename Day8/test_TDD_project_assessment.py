from TDD_project_assessment import Todo


def test_add_task():
    t = Todo()
    t.add("Study")
    assert "Study" in t.tasks


def test_remove_task():
    t = Todo()
    t.add("Study")
    t.remove("Study")
    assert "Study" not in t.tasks


def test_list_tasks():
    t = Todo()
    t.add("Study")
    t.add("Exercise")
    assert t.list_tasks() == ["Study", "Exercise"]
