# CPSC 2030 (Lab_05)

**Instructions**  
For this lab, you will gain additional exposure to working with inheritance in Python. To do this, we will simulate a streaming service that allows users to watch movies and shows. I have provided `main.py`, which uses input files containing information for movies and shows.

You should satisfy the following requirements:
- Create a file called `media.py` that contains class definitions for MediaContent (base class), Movie (derived), TVShow (derived), and StreamingService (base).
  - MediaContent should have the following
    - Attributes: title (string), genre (string), rating (string), runtime (integer, minutes), cast (list of strings)
    - Methods
      - __init__() 
      - get_info(): Print a message that includes the title, genre, and the cast member in the list.
      - get_runtime(): Return the runtime
  - Movie should have the following
    - Attributes:  All from MediaContent plus release_year (integer)
    - Methods
      - __init__(): Uses super() for MediaContent init
      - play(): Print the title, rating, and release year.
  - TVShow should have the following
    - Attributes: All from MediaContent plus num_seasons (integer)
    - Methods
      - __init__(): Uses super() for MediaContent init
      - play(): Print the title and number seasons.
  - StreamingService should have the following
    - Attributes: available_content (list)
    - Methods
      - add_content: Appends new item (whether Movie or TVShow) to the list and prints a message using the title
      - remove_content: Removes identified item from available_content and prints a message using the title
      - watch: Checks to see if the selection is present in available_content. If present, calls the play() function, otherwise prints a message.
- Use GitHub appropriately
  - For this lab, it is acceptable to simply commit changes to the `main` branch.
  - Show multiple commits as you get the program working.
