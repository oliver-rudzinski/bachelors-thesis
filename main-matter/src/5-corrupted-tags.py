def test_xml_corrupted_tags(self):
    s3_client = client("s3")
    test_collection = prefix.format("corrupted.xml")

    mock_dict = {
        obj.key.split("/")[-1]: obj.get()["Body"].read()
        for obj in bucket.objects.filter(Prefix=test_collection)
        if not obj.key.split("/")[-1] == ""
    }

    xml_to_dict(mock_dict)
    tag = s3_client.get_object_tagging(
        Bucket=bucket.name, Key=test_collection,
    )["TagSet"]

    assert {"Key": "xmlCorr-err", "Value": "True"} in tag