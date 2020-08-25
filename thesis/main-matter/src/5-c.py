def check_global_attrs(self, dicts):
    for name, poslog_dict in dicts.items():
        if all(attr in poslog_dict.keys() for attr in self.global_attrs):
            continue

        # Data handling for required attributes omitted...

        if not all(
            attr in poslog_dict.keys() for attr in self.opt_global_attrs
        ):
            missing_attrs = list(
                (set(self.opt_global_attrs) - poslog_dict.keys())
            )
            self.logger.warning(
                'Missing optional global attribute(s) | File '
                'Name: "{}" '
                'Missing Attribute(s): {}'.format(
                    name, ', '.join(missing_attrs)
                )
            )
            self.warning_files += 1
            self._set_file_tags(
                    self.src_bucket,
                    f"{self.src_dir}{name}",
                    "optArg-warn",
                )