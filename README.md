# Scrappy  
**_Scrappy_** is a super customizable yet simple web scraper!  
  
## What Is It?  
 
 <div style="background-color: #FFCCCC; color: #333; padding: 15px; border-radius: 50px; border: 1px solid #FF9999;">
  <strong style="font-size: 1.2em;">⚠️ DISCLAIMER:</strong> The terminology/names may change or be different in actual code. As features are added, example code and explanations will be added. 
</div>

 ***Scrappy*** heavily borrows from OOP concepts, so that there are *Site*, *Media*, and *Content* objects. *Site* objects are basically a way to classify sites and specifics about them. For example, some sites may have unique codes in their URL for content pages (eg: manga sites with /(manga_id)/(page_number) ) and lets you define them. *Media* objects will be built in classes that will make it easy to parse common data types such as text or images. *Content* objects will just be the readable/adjustable *Media* objects that may be needed in case a site can't be scraped through the regular methods.