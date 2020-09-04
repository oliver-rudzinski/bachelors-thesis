def test_xml_corrupted_logs(self, caplog):
    test_collection = prefix.format("corrupted.xml")

    mock_dict = {
        obj.key.split("/")[-1]: obj.get()["Body"].read()
        for obj in bucket.objects.filter(Prefix=test_collection)
        if not obj.key.split("/")[-1] == ""
    }

    with caplog.at_level(logging.ERROR, logger=__name__):
        xml_to_dict(mock_dict)

    assert "XML File Corrupted" in caplog.text