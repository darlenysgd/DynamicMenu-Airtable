# DynamicMenu-Airtable
Tech Pirate Homework Assignment - Resonance

To run de python app you'll need some packages that are listed in the the main directory in the "requirements.txt" file, you can install them individually or in a virtual environment.

Based on the mission provided that consist on build a dynamic menu using the links and menu ontology provided in an Airtable base I have accomplished the fallowing goals:

1. Consume the Airtable API and build a dynamic menu with the data given:
   To accomplish this goal I used python3, since I noticed is a main programming language in Resonance. In the code I'm making a    request to the Airtable API using my API KEY and the BASE KEY and then transform de data given to build a structure that        facilitates to render the menu in the user interface.
2. Develop a user interface to render the menu:
  For this I used Flask, a microframework for Python and Bootstrap to style the menu. In the main directory you can see a file   called "DynamicMenuWeb" with the results.
3. Develop a Google Crhome Extension:
  To accomplish this I consumed my python app to get the transformed data and used Javascript to append the menu elements to     the HTML and algo CSS to add the style. I uploaded it to Crhome following their documentation, that consist in create the       manifest.json and reference the directory in the Crhome Extension section when is developer mode. In the main directory you     can see a file called "DynamicMenuExtension" with the result.
  
Excluding Python and Bootstrap it was my first time applying these technologies and I can say that it was really interesting, challenging and fun to work with in this task. 

I hope that I have met your expectations towards me in this assigment.

Thank you for the opportunity.

Darlenys G.
  
