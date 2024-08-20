# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from start.items import StartItem,SecondItem

class StartPipeline:
    def process_item(self, item, spider):
        if isinstance(item,SecondItem):
            adapter=ItemAdapter(item)

            if 'order' in adapter:
                order=adapter.get('order')
                order+=1

                adapter['order']=order
            else:
                print('there is no order')
                
        return item
