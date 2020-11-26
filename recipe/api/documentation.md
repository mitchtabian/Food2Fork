# Endpoints
1. [Searching for recipes](#Search-Recipes)
1. [Find by Recipe ID](#Find-by-Recipe-ID)

<br>

# Search Recipes
Keyword search for recipes.

<br>

#### GET 
```
https://food2fork.ca/api/recipe/search/?page=2&query=beef carrot potato onion
```

<br>

#### Headers
| Key | Value |
|-----|-------|
| Authorization | Token 9c8b06d329136da358c2d00e76946b0111ce2c48|

<br>

#### Success Response
```json
{
    "count": 44,
    "next": "https://food2fork.ca/api/recipe/search/?page=3&query=beef+carrot+potato+onion",
    "previous": "https://food2fork.ca/api/recipe/search/?query=beef+carrot+potato+onion",
    "results": [

		{
			"pk": 2050,
			"title": "Chicken, sweet potato &amp; coconut curry",
			"publisher": "jessica",
			"featured_image": "https://food2fork.ca//media/featured_images/2050/featured_image.png",
			"rating": 50,
			"source_url": "http://www.bbcgoodfood.com/recipes/1555/chicken-sweet-potato-and-coconut-curry",
			"description": "N/A",
			"cooking_instructions": null,
			"ingredients": {
				"175g frozen peas": "",
				"300ml chicken stock": "",
				"1 tbsp sunflower oil": "",
				"2 tsp mild curry paste": "",
				"400ml can coconut milk": "",
				"4 tbsp red split lentils": "",
				"2 medium-sized sweet potatoes , peeled and cut into bite-size pieces": "",
				"2 large boneless, skinless chicken breasts , cut into bite-size pieces": ""
			},
			"date_added": "2020-11-26T00:07:32.114943Z",
			"date_updated": "2020-11-26T00:07:32.114403Z"
		},
		{
			"pk": 9,
			"title": "Avocado Egg Salad",
			"publisher": "maizy",
			"featured_image": "https://food2fork.ca/media/featured_images/9/featured_image.png",
			"rating": 69,
			"source_url": "http://www.twopeasandtheirpod.com/avocado-egg-salad/",
			"description": "N/A",
			"cooking_instructions": null,
			"ingredients": {
				"1/4 teaspoon Dijon mustard": "",
				"2 hard boiled eggs, chopped": "",
				"1 tablespoon fresh lemon juice": "",
				"2 hard boiled egg whites, chopped": "",
				"2 tablespoons chopped green onion": "",
				"2 small avocados, pitted and peeled": "",
				"Salt and freshly ground black pepper, to taste": "",
				"1 tablespoon plain Greek yogurt (we use Chobani)": ""
			},
		"date_added": "2020-11-25T23:58:35.240032Z",
		"date_updated": "2020-11-25T23:58:35.239712Z"
		},
	]
}
```

<br>

#### No Results
```json
{
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}
```

<br>

#### Failure
```
<Exception message>
```

<br>

# Find by Recipe ID
Find a specific recipe by referencing its unique id.

<br>

#### GET 
```
https://food2fork.ca/api/recipe/get/?id=9
```

<br>

#### Headers
| Key | Value |
|-----|-------|
| Authorization | Token 9c8b06d329136da358c2d00e76946b0111ce2c48|

<br>

#### Success Response
```json
{
    "pk": 9,
    "title": "Avocado Egg Salad",
    "publisher": "maizy",
    "featured_image": "https://food2fork.ca//media/featured_images/9/featured_image.png",
    "rating": 69,
    "source_url": "http://www.twopeasandtheirpod.com/avocado-egg-salad/",
    "description": "N/A",
    "cooking_instructions": null,
    "ingredients": {
        "1/4 teaspoon Dijon mustard": "",
        "2 hard boiled eggs, chopped": "",
        "1 tablespoon fresh lemon juice": "",
        "2 hard boiled egg whites, chopped": "",
        "2 tablespoons chopped green onion": "",
        "2 small avocados, pitted and peeled": "",
        "Salt and freshly ground black pepper, to taste": "",
        "1 tablespoon plain Greek yogurt (we use Chobani)": ""
    },
    "date_added": "2020-11-25T23:58:35.240032Z",
    "date_updated": "2020-11-25T23:58:35.239712Z"
}
```

<br>

#### Failure
```
<Exception message>
```


