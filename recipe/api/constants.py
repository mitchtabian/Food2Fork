from enum import Enum

class ApiRecipeResponse(Enum):
	INVALID_RECIPE_ID = "Invalid Recipe id."
	INTEGER_RECIPE_ID = "Recipe id must be an integer."
	RECIPE_DOES_NOT_EXIST = "A Recipe matching that id does not exist."
	UNKNOWN_ERROR = "An unknown error occurred. Contact the developer."




