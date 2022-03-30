---
# An instance of the Contact widget.
# Documentation: https://sourcethemes.com/academic/docs/page-builder/
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 130

title: Contact
subtitle:

content:
  # Automatically link email and phone or display as text?
  autolink: true
  
  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: true 

# Contact (edit or remove options as required)

email: mwagner@ucsd.edu
phone: ''
address:
  street: 10010 N Torrey Pines Rd
  city: La Jolla
  region: CA
  postcode: '92037'
  country: United States
  country_code: US
coordinates:
    latitude: '32.8867'
    longitude: '-117.2461'
directions: ''
appointment_url: ''
contact_links:
  - icon: envelope
    icon_pack: fas 
    name: mwagner92796@gmail.com
    links: mailto:mwagner92796@gmail.com
#contact_links:
#  - icon: linkedin-in
#    icon_pack: fab
#    name: Connect with me
#    link: 'https://www.linkedin.com/in/margot-wagner/'
  
design:
  columns: '2'
---
