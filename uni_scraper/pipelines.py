class CleanPipeline:

    def process_item(self, item, spider):
        if item.get("email"):
            item["email"] = item["email"][0] if isinstance(item["email"], list) else item["email"]

        return item
