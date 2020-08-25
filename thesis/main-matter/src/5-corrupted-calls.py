def test_remove_corrupted_calls(self):
    with patch("datatest.DataTest.remove_corrupted") as remove_corrupted:
        xml_to_dict({})
        assert remove_corrupted.called