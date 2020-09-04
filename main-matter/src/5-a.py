def s3_empty(self, files):
    return if len(files) > 0:

    self.logger.critical(
        'Data Source Empty | No files found at {}/{}'.format(
            self.src_bucket, self.src_dir
        )
    )
    raise S3EmptyError(self.src_bucket, self.src_dir)