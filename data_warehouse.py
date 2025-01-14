
grammar_words = [
            'a', 'an', 'the', 'some', 'any', 'all', 'many', 'few', 'much', 'more', 'most', 
            'little', 'a little', 'a lot of', 'each', 'every', 'either', 'neither', 'this', 
            'that', 'these', 'those', 'it', 'he', 'she', 'they', 'we', 'you', 'me', 'him', 
            'her', 'us', 'them', 'myself', 'herself', 'himself', 'itself', 'ourselves', 
            'yourselves', 'themselves', 'who', 'which', 'that', 'whose', 'am', 'is', 'are', 
            'was', 'were', 'be', 'being', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 
            'will', 'would', 'shall', 'should', 'may', 'might', 'can', 'could', 'must', 
            'ought', 'dare', 'need', 'used', 'go', 'goes', 'went', 'gone', 'going', 'make', 
            'makes', 'made', 'let', 'lets', 'letting', 'has been', 'had been', 'will be', 
            'would be', 'shall be', 'should be', 'can be', 'could be', 'must be', 'always', 
            'often', 'sometimes', 'rarely', 'never', 'slowly', 'quickly', 'carefully', 
            'happily', 'sadly', 'here', 'there', 'where', 'everywhere', 'anywhere', 'now', 
            'then', 'when', 'soon', 'later', 'very', 'really', 'quite', 'extremely', 'too', 
            'and', 'but', 'or', 'for', 'nor', 'so', 'yet', 'because', 'since', 'although', 
            'while', 'unless', 'after', 'before', 'until', 'as', 'if', 'in', 'on', 'at', 
            'to', 'from', 'by', 'with', 'through', 'about', 'above', 'across', 'against', 
            'beneath', 'beside', 'between', 'beyond', 'during', 'except', 'inside', 
            'outside', 'under', 'unlike', 'upon', 'not', "n't", 'lol', 'brb', 'tldr', 'idk', 
            'omg', 'ads'
        ]
search_by = ["search by", "text in image", "brand in image",
            "object in image", "celebrity in image"]
sort_by = ["sort by", "Likes", "Shares", "Comments", "Impressions", "Popularity"]
call_to_action = ["call to action", "Add", "Add to Cart", "Apply Now", "Ask", "Assist", "Book Now", "Buy", "Buy Now", "Buy Tickets",
            "Call", "Call Now", "Chat with Us", "Check", "Contact Us", "Continue", "Contribute", "Donate",
            "Donate Now", "Download", "Email Now", "Find More", "Follow", "Get Access", "Get Coupon", "Get Deal",
            "Get Directions", "Get Offer", "Get Quote", "Get Showtimes", "Get Tickets", "Get Trends", "Get Your Code",
            "Give Now", "Go Now", "Go Shopping", "Grab a Bid", "Hear", "Install", "Install App", "Install Now",
            "Interested", "Join", "Know More", "Learn More", "Like Page", "Like This Page", "Listen Now",
            "Look More", "Make an Order", "Menu", "Message", "More", "More on This", "Obtain Offer", "Offer",
            "Open Link", "Order Now", "Play Game", "Play Now", "Purchase", "Read", "Register Now", "Request Time",
            "Reserve Now", "Save", "Save Offer", "Schedule", "Search", "See Details", "See Menu", "See More",
            "Sell Now", "Send", "Send Message", "Shop Now", "Sign Up", "Start Order", "Subscribe", "Try In Camera",
            "Try It", "Turn on Us", "Use App", "Use the Offer", "View", "View Event", "Visit Website", "Vote Now",
            "Watch More", "Watch Others", "Watch Video"]
search_ads_by_country = ['search_ads_by_country','America', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', "Côte d'Ivoire", 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'DR Congo', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts & Nevis', 'Saint Lucia', 'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Vincent & Grenadines', 'State of Palestine', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', 'Aland Islands', 'American Samoa', 'Anguilla', 'Antarctica', 'Antigua And Barbuda', 'Aruba', 'The Bahamas', 'Bermuda', 'Bouvet Island', 'British Indian Ocean Territory', 'Cape Verde', 'Cayman Islands', 'Christmas Island', 'Cocos (Keeling) Islands', 'Democratic Republic of the Congo', 'Cook Islands', "Cote D'Ivoire", 'East Timor', 'Falkland Islands', 'Faroe Islands', 'Fiji Islands', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gambia The', 'Gibraltar', 'Greenland', 'Guadeloupe', 'Guam', 'Guernsey and Alderney', 'Heard Island and McDonald Islands', 'Hong Kong S.A.R.', 'Jersey', 'Macau S.A.R.', 'Man (Isle of)', 'Martinique', 'Mayotte', 'Montserrat', 'Bonaire, Sint Eustatius and Saba', 'New Caledonia', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Palestinian Territory Occupied', 'Papua new Guinea', 'Pitcairn Island', 'Puerto Rico', 'Reunion', 'Saint Helena', 'Saint Kitts And Nevis', 'Saint Pierre and Miquelon', 'Saint Vincent And The Grenadines', 'Saint-Barthelemy', 'Saint Martin', 'Sao Tome and Principe', 'South Georgia', 'Svalbard And Jan Mayen Islands', 'Swaziland', 'Taiwan', 'Tokelau', 'Trinidad And Tobago', 'Turks And Caicos Islands', 'United States Minor Outlying Islands', 'Vatican City State', 'Virgin Islands', 'Virgin Islands', 'Wallis And Futuna Islands', 'Western Sahara', 'Kosovo', 'CuraÃ§ao', 'Sint Maarten']

ad_type = ["ad type", "Image", "video"]
ad_position = ["ad position", "News Feed",
               "Side Column", "Video Feed", "Marketplace"]
affiliate_network = ["affiliate network", "Amazon Associates", "AvanGate", "AWIN", "ClickBank", "eBay Partner Network (EPN)", "GiddyUp", "Impact",
                     "LeadDyno", "LinkConnector", "Partnerstack", "Pepperjam", "Rakuten", "Refersion", "ShareASale", "SKIMLINKS"]
ecommerce_platform = ["ecommerce_platform", "3DCart", "BigCommerce", "Demandware", "Magento", "PrestaShop", "Shopify", "Squarespace", "Volusion", "Wix",
                      "WooCommerce"]
funnel = ["funnel", "Builderall", "ClickFunnels", "Convertri", "GetResponse", "Instapage", "Kajabi", "Kartra", "Keap", "Landingi", "LeadPages",
          "OptimizePress", "SamCart", "Wishpond", "Any"]
marketing_platform = ["marketing_platform", "Adobe Audience Manager", "Branch", "Conversionx", "Google Marketing Platform", "Hootsuite", "HubSpot",
                      "Kenshoo", "Neustar"]
source = ["source", "Android", "Desktop", "iOS", "All"]
postwise = ["postwise", "Hide advertizer", "Hide this ad"]
platforms = ["platforms", "Quora", "Instagram", "Youtube", "Google",
            "GDN", "Native", "Pinterest", "Linkedin", "Reddit", "Facebook"]
ad_category = ["ad category","Abortion", "Adult/Mature Content", "Alcohol", "Alternative Spirituality/Belief", 
            "Art/Culture", "Auctions", "Audio/Video Clips", "Brokerage/Trading", "Business/Economy",
            "Charitable/Non-Profit", "Chat (IM)/SMS", "Cloud Infrastructure", "Compromised Sites",
            "Computer/Information Security", "Content Delivery Networks", "Controlled Substances",
            "Cryptocurrency", "Dynamic DNS Host", "E-Card/Invitations", "Education", "Email",
            "Email Marketing", "Entertainment", "File Storage/Sharing", "Finance", "For Kids",
            "Gambling", "Games", "Gore/Extreme", "Government/Legal", "Hacking", "Health",
            "Humor/Jokes", "Informational", "Internet Connected Devices", "Internet Telephony",
            "Intimate Apparel/Swimsuit", "Job Search/Careers", "Malicious Outbound Data/Botnets",
            "Malicious Sources/Malnets", "Marijuana", "Media Sharing", "Military",
            "Mixed Content/Potentially Adult", "News", "Newsgroups/Forums", "Nudity",
            "Office/Business Applications", "Online Meetings", "Peer-to-Peer (P2P)", "Personal Sites",
            "Personals/Dating", "Phishing", "Piracy/Copyright Concerns", "Placeholders",
            "Political/Social Advocacy", "Potentially Unwanted Software", "Proxy Avoidance",
            "Radio/Audio Streams", "Real Estate", "Reference", "Religion", "Remote Access",
            "Restaurants/Food", "Scam/Questionable Legality", "Search Engines/Portals",
            "Sex Education", "Shopping", "Social Networking", "Society/Daily Living",
            "Software Downloads", "Spam", "Sports/Recreation", "Suspicious", "Technology/Internet",
            "Tobacco", "Translation", "Travel", "TV/Video Streams", "Uncategorized", 
            "URL Shorteners", "Vehicles", "Violence/Intolerance", "Weapons", "Web Ads/Analytics","Web Hosting", "Web Infrastructure"]
image_logo = ['image_logo',
            "Accenture", "Adidas", "Ajio", "Allianz", "Amazon", "Apple", "Audi", "AXA", "BMW", "Budweiser",
            "Cartier", "Chanel", "Cisco", "Citi", "ClickCease", "Coca Cola", "Colgate", "Dell", "Designrr",
            "DHL", "Dior", "Discovery", "Disney", "eBay", "Facebook", "FedEx", "Ferrari", "Flipkart", "Ford",
            "Gillette", "Giva", "Goldman Sachs", "Google", "Gucci", "Heineken", "Hennessy", "Hermes", "HP",
            "HSBC", "IBM", "IKEA", "Intel", "iPhone", "Jack Daniels", "JioMart", "John Deere", "Johnson",
            "Kajabi", "Kellogg's", "KFC", "Kia", "Land Rover", "LEGO", "LinkedIn", "L'Oréal", "Louis Vuitton",
            "Marvel", "McDonald's", "Meesho", "Mercedes", "Microsoft", "Mini", "Morgan Stanley", "Motorola",
            "Nescafe", "Nestle", "Netflix", "Nexon", "Nike", "Nintendo", "Nivea", "Novakid", "Nykaa", "Oracle",
            "Pampers", "Panasonic", "Pepsi", "Plum", "Prada", "Puma", "Reebok", "Samsung", "Shell", "Shopify",
            "Siemens", "Simplilearn", "Sony", "Spotify", "Swiggy", "Toyota", "TVS", "Uber", "UpGrad", "Visa",
            "Wells Fargo", "Zara", "Zomato"
        ]

image_object = ['image object',
            "Aeroplane", "Airplane", "Apple", "Banana", "Bank card", "Baseball bat", "Baseball glove", "Bear",
            "Bed", "Bench", "Bicycle", "Bike", "Bird", "Boat", "Book", "Bottle", "Bottom wear", "Bowl", "Broccoli",
            "Burger", "Bus", "Cake", "Camera", "Cap", "Car", "Carrot", "Cat", "Cell phone", "Chair", "Clock",
            "Coffee machine", "Cosmetic cream", "Couch", "Cow", "Cricket bat", "Cup", "Dining table", "Dining table",
            "Dog", "Donut", "Elephant", "Face mask", "Fire hydrant", "Flower", "Fork", "Frisbee", "Fruit", "Game remote",
            "Giraffe", "Glass", "Gym equipment", "Handbag", "Headset", "Helmet", "Horse", "Horseshoe", "Hot dog",
            "Jewellery", "Keyboard", "Kite", "Laptop", "Laptop bag", "Lion", "Microwave", "Mobile", "Motorbike",
            "Motorcycle", "Mouse", "Orange", "Oven", "Parking meter", "Pen", "Perfume", "Person", "Pizza", "Plant",
            "Potted plant", "Refrigerator", "Remote", "Sandwich", "Saree", "Scissors", "Sheep", "Shoes", "Sink",
            "Skateboard", "Ski", "Snowboard", "Sofa", "Speakers", "Spectacles", "Spoons", "Sports ball", "Stop sign",
            "Suitcase", "Surfboard", "Table", "Tablet", "Teddy", "Teddy bear", "Tennis racket", "Tie", "Tiger", "Toilet",
            "Toothbrush", "Toothbrush", "Top wear", "Toys", "Traffic light", "Train", "Trimmer", "Truck", "TV", "TV remote",
            "TV monitor", "Umbrella", "Vase", "Vehicle tyres", "Wine glass", "Zebra"
    ]

image_celebrity = ['image celebrity',
            "Aamir Khan", "Aaron Donald", "Abhay Deol", "Adam Sandler", "Ajay Devgn", "Ajay Piramal", "Akhilesh Yadav",
            "Akshay Kumar", "Alexis Sanchez", "Ali Fazal", "Alia Bhatt", "Allu Arjun", "Amish Tripathi", "Amit Shah",
            "Amit Trivedi", "Anand Mahindra", "Andres Iniesta", "Andy Murray", "Angelina Jolie", "Anil Kapoor",
            "Anthony Joshua", "Anupam Kher", "Anushka Sharma", "AR Rahman", "Arbaaz Khan", "Ariana Grande", "Arijit Singh",
            "Arjun Kapoor", "Arshad Warsi", "Arun Jaitley", "Asha Parekh", "Ashok Gehlot", "Ashok Saraf", "Ashutosh Rana",
            "Asrani", "Athiya Shetty", "Avtar Gill", "Axar Patel", "Azim Premji", "Babul Supriyo", "Badshah", "Barack Obama",
            "Barinder Sran", "Barun Sobti", "Bhagwant Mann", "Bharti Singh", "Bhumi Pednekar", "Bhumika Chawla",
            "Bhupesh Baghel", "Bipasha Basu", "Brad Pitt", "Bradley Cooper", "Bruce Lee", "Calvin Harris", "Canelo Alvarez",
            "Carson Wentz", "Celine Dion", "Cesc Fabregas", "Chetan Bhagat", "Chris Evans", "Chris Paul", "Conor McGregor",
            "Daisy Shah", "Dalip Tahil", "Damian Lillard", "Dani Alves", "David De Gea", "Deontay Wilder", "Dev Anand",
            "Diana Penty", "Dilip Joshi", "Dilip Kumar", "Dilip Shanghvi", "Diljit Dosanjh", "Dinesh Karthik", "Disha Patani",
            "Divya Bharti", "Divya Spandana", "DJ Khaled", "Drake", "Drew Brees", "Dwayne Johnson", "Dwight Howard",
            "Dwyane Wade", "Ed Sheeran", "Eden Hazard", "Elton John", "Eminem", "Emma Stone", "Emma Watson", "Esha Gupta",
            "Farah Khan", "Farhan Akhtar", "Farida Jalal", "Fumi Nikaido", "Gareth Bale", "Gauhar Khan", "Gautam Adani",
            "Gautam Gambhir", "Gerard Pique", "Gordon Ramsay", "Govinda", "Hardik Pandya", "Hardik Patel", "Harrison Ford",
            "Harsh Mariwala", "Hema Malini", "Hemant Soren", "Honey Singh", "Howard Stern", "Hrithik Roshan", "Hugh Jackman",
            "Huma Qureshi", "Imran Khan", "Irfan Pathan", "Irrfan Khan", "Ishaan Khatter", "Jackie Chan", "James Harden",
            "Jasprit Bumrah", "Jay Z", "Jaya Bhaduri", "Jaydev Unadkat", "Jennifer Lopez", "Jerry Seinfeld", "Jessica Alba",
            "Jimmy Buffett", "Jitendra Singh", "Joe Biden", "John Abraham", "Johnny Depp", "Johnny Lever", "Jordan Spieth",
            "Judy Sheindlin", "Juhi Chawla", "Junior NTR", "Justin Bieber", "Kabir Bedi", "Kajal Aggarwal", "Kajol",
            "Kalki Koechlin", "Kamal Nath", "Kangana Ranaut", "Kanye West", "Kapil Sharma", "Karan Grover", "Karan Johar",
            "Karan Kundra", "Karim Benzema", "Kartik Aaryan", "Katrina Kaif", "Katy Perry", "KCR", "Keanu Reeves",
            "Kendrick Lamar", "Kevin Durant", "Kevin Hart", "Khalil Mack", "Kiara Advani", "Kim Kardashian", "Kiren Rijiju",
            "Kishore Biyani", "Kishore Kumar", "Kit Harington", "KL Rahul", "Klay Thompson", "Konkona Sen", "Kriti Sanon",
            "Kunal Khemu", "Kylian Mbappe", "Kylie Jenner", "Kyrie Irving", "Lady Gaga", "LeBron James", "Lewis Hamilton",
            "Lionel Messi", "Luka Modric", "Luke Bryan", "M K Stalin", "Madhoo", "Madhuri Dixit", "Mahesh Babu", "Mamta Kulkarni",
            "Manish Pandey", "Manish Paul", "Manmohan Singh", "Manoj Bajpayee", "Manoj Tiwari", "Marcelo Vieira", "Meena Kumari",
            "Megan Fox", "Meiyang Chang", "Mel Gibson", "Mesut Ozil", "Mika Singh", "Mohamed Salah", "Mohammad Kaif",
            "Mohammed Shami", "Mohan Agashe", "Mohanlal", "Mohit Sharma", "Mohnish Bahl", "MS Dhoni", "Mukesh Ambani",
            "Nakuul Mehta", "Nana Patekar", "Narendra Modi", "Naveen Patnaik", "Nayanthara", "Neha Dhupia", "Neha Sharma",
            "Neymar", "Ninja", "Nitin Gadkari", "Nitish Kumar", "Novak Djokovic", "Omi Vaidya", "Paresh Rawal", "Paul George",
            "Paul McCartney", "Paul Pogba", "Paul Rudd", "Paulo Dybala", "Pawan Kalyan", "Phil McGraw", "Phil Mickelson", "Pink",
            "Piyush Goyal", "Prabhas", "Prabhu Deva", "Prachi Desai", "Prakash Raj", "Pran", "Preity Zinta", "PV Sindhu",
            "Raaj Kumar", "Radhika Apte", "Rafael Nadal", "Rahul Dev", "Rahul Gandhi", "Raima Sen", "Raj Thackeray", "Rajinikanth",
            "Rajkumar Rao", "Rajpal Yadav", "Rakesh Bedi", "Ram Charan", "Ram Madhav", "Rana Daggubati", "Ranbir Kapoor",
            "Rani Mukerji", "Ranveer Singh", "Ranvie Shorey", "Rati Agnihotri", "Raveena Tandon", "Ravi Shastri", "Rekha",
            "Richa Chadda", "Rihanna", "Rishabh Pant", "Rob Gronkowski", "Roger Federer", "Rohit Roy", "Rohit Sharma",
            "Ronit Roy", "Rory Mcllroy", "Rush Limbaugh", "Russell Wilson", "Ryan Reynolds", "Ryan Seacrest", "Sachin Pilot",
            "Saif Ali Khan", "Saina Nehwal", "Salim Merchant", "Salman Khan", "Sandra Bullock", "Sanjay Dutt", "Sanjay Mishra",
            "Sanjeev Kapoor", "Sanjiv Goenka", "Sanya Malhotra", "Sara Ali Khan", "Satish Kaushik", "Sayaji Shinde",
            "Sean Combs", "Sean Hannity", "Sergio Aguero", "Sergio Ramos", "Shahid Kapoor", "Shahrukh Khan", "Shakti Kapoor",
            "Shamita Shetty", "Sharad Pawar", "Shardul Thakur", "Sharman Jhosi", "Shashi Kapoor", "Shashi Tharoor",
            "Shaun White", "Shawn Mendes", "Shikhar Dhawan", "Shreyas Iyer", "Shubman Gill", "Smita Patil", "Sofía Vergara",
            "Sonakshi Sinha", "Sonali Bendre", "Sonam Kapoor", "Sonia Gandhi", "Sonu Sood", "Sridevi", "Sridhar Vembu",
            "Stephen Curry", "Steve Harvey", "Suchitra Sen", "Sudeep", "Sumeet Vyas", "Suniel Shetty", "Sunil Gavaskar",
            "Sunil Grover", "Sunil Joshi", "Sunny Deol", "Suraj Pancholi", "Suresh Raina", "Suriya", "Sushma Swaraj",
            "Taapsee Pannu", "Tabu", "Taylor Swift", "The Weeknd", "Tiger Shroff", "Tiger Woods", "Tiku Talsania", "Tinu Yohannan",
            "Tom Brady", "Tom Cruise", "Toni Kroos", "Travis Scott", "TTV Dhinakaran", "Twinkle Khanna", "Tyson Fury",
            "Uday Kotak", "Umesh Yadav", "V K Singh", "Varun Dhawan", "Varun Sharma", "Vicky Kaushal", "Vidya Balan",
            "Vidyut Jammwal", "Vijay", "Vijay Shankar", "Vijender Singh", "Vikram", "Vikrant Massey", "Vin Diesel",
            "Virat Kohli", "Vivek Oberoi", "Wasim Jaffer", "Wayne Rooney", "Will Smith", "Yami Gautam", "Yashpal Sharma",
            "Yusuf Pathan", "Yuvraj Singh", "Zaheer Khan"
]

seen_btn_sort=[
             "seen between sort", "seen btn sort", "seen btn", "seen between"
]
post_date_btn_sort=[
              "post date between sort", "post date btn sort", "post date btn", "post date between", "postdate between", "postdate btn","postdate between"
]
domain_date_btn_sort=[
              "domain date between sort", "domain date btn sort", "domain date btn", "domain date between", "domaindate between", "domaindate btn","domaindate between"
]
languages = ["languages","(Afan)/Oromoor/Oriya", "Abkhazian", "Afar", "Afrikaans", "Albanian", "Amharic", "Arabic", "Aragonese", "Armenian", "Assamese", "Avaric", "Aymara", "Azerbaijani", "Bashkir", "Basque", "Belarusian", "Bengali", "Bhutani", "Bihari", "Bislama", "Bosnian", "Breton", "Bulgarian", "Burmese", "Cambodian", "Catalan", "Chechen", "Chinese", "Chuvash", "Cornish", "Corsican", "Croatian", "Czech", "Danish", "Dummy", "Dutch", "English", "Esperanto", "Estonian", "Faeroese", "Fiji", "Finnish", "French", "Frisian", "Galician", "Georgian", "German", "Greek", "Greenlandic", "Guarani", "Gujarati", "Haitian creole", "Hausa", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Ido", "Indonesian", "Interlingua", "Interlingue", "Inupiak", "Irish", "Italian", "Japanese", "Javanese", "Kannada", "Kashmiri", "Kazakh", "Kinyarwanda", "Kirghiz", "Kirundi", "Korean", "Kurdish", "Laothian", "Latin", "Latvian/Lettish", "Limburgan", "Lingala", "Lithuanian", "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maldivian", "Maltese", "Manx", "Maori", "Marathi", "Moldavian", "Mongolian", "Nauru", "Nepali", "Norwegian", "Norwegian Nynorsk", "Occitan", "Odia", "Ossetian", "Pashto/Pushto", "Persian", "Polish", "Portuguese", "Punjabi", "Quechua", "Rhaeto-Romance", "Romanian", "Russian", "Samoan", "Sangro", "Sanskrit", "Scots/Gaelic", "Serbian", "Serbo-Croatian", "Sesotho", "Setswana", "Shona", "Sindhi", "Singhalese", "Siswati", "Slovak", "Slovenian", "Somali", "Spanish", "Sundanese", "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tibetan", "Tigrinya", "Tonga", "Tsonga", "Turkish", "Turkmen", "Twi", "Ukrainian", "Urdu", "Uyghur", "Uzbek", "Vietnamese", "Volapuk", "Walloon", "Welsh", "Wolof", "Xhosa", "Yiddish", "Yoruba", "Zulu"]

list_of_postOwner=["post owner",'aa', 'Jeffi', 'Xank.in', 'TouchPal', 'Hublot','Louis Vuitton Official', 'PeeSafe', 'Sweetselfie_official',
       'TOYOTA GLOBAL', 'Etihad Airways', 'Nua', 'Visa',  'Alex Mehr, Ph.D.', 'ONLY India', 'Z3 Online', 'WeetoHair',
       'StarMaker - Sing & Connect Wit', 'Koryo', 'Kwai', "Vitabiotics", "samsung", 'Nykaa', "Muscleblaze"
       ]

list1 = [
        domain_date_btn_sort,   seen_btn_sort, 
        post_date_btn_sort,     platforms,search_by, 
        sort_by,                call_to_action, 
        search_ads_by_country,  ad_type, 
        ad_position,            image_logo,image_object, 
        image_celebrity,        affiliate_network, 
        ecommerce_platform,     funnel, 
        marketing_platform,     source, 
        postwise,   ad_category, list_of_postOwner, grammar_words
        ]

full_list=[w.lower() for inner_list in list1 for w in inner_list]


sample_searches = [
    # Incomplete phrases 
    "I want",
    "I want see",
    
    # General Searches
    "Show all ads",
    "Show me some ads from"
    # Show ads by network
    "Show ads on Facebook",
    "Display Instagram ads",
    "List all YouTube ads",
    
    # Show ads by advertiser
    "Show ads by Nykaa",
    "Display Samsung ads",
    "List Muscleblaze ads",
    "Show ads from Vitabiotics",
    
    # Show ads by network and advertiser
    "Show Nykaa ads on Facebook",
    "Display Samsung ads on Instagram",
    "List Muscleblaze ads on YouTube",
    "Show Vitabiotics ads on Instagram",
    
    # Show ads by country
    "Show ads in the United States",
    "Display ads in India",
    "List ads in the United Kingdom",
    "Show ads in Australia",
    
    # Show ads by network, advertiser, and country
    "Show Nykaa ads on Facebook in India",
    "Display Samsung ads on Instagram in the United States",
    "List Muscleblaze ads on YouTube in the United Kingdom",
    "Show Vitabiotics ads on Instagram in Australia",
    
    # Show market analytics
    "Show market analytics for Facebook ads",
    "Display market analytics for Nykaa",
    "List market analytics for YouTube ads in the United States",
    "Show market analytics for Samsung ads on Instagram",
    
    # Show ads or analytics for a specific time period
    "Show Nykaa ads on Facebook from last month",
    "Display Samsung ads on Instagram for the past year",
    "List Muscleblaze ads on YouTube for January 2024",
    "Show market analytics for Vitabiotics ads on Instagram in Q1 2024",
    
    # Combining multiple filters
    "Show Nykaa ads on Facebook in India for the past month",
    "Display Samsung ads on Instagram in the United States for the last quarter",
    "List Muscleblaze ads on YouTube in the United Kingdom for the year 2023",
    "Show market analytics for Vitabiotics ads on Instagram in Australia for the past year"

    "Show ads on Facebook in the United States",
    "Display Instagram ads in India",
    "List YouTube ads in the United Kingdom",
    "Show ads on Facebook in Australia",
    "Display Instagram ads in Canada",
    "List YouTube ads in Germany",
    "Show ads on Facebook in France",
    "Display Instagram ads in Japan",
    "List YouTube ads in South Korea",
    "Show ads on Facebook in Brazil",
    "Display Instagram ads in Italy",
    "List YouTube ads in Spain",
    "Show ads on Facebook in Mexico",
    "Display Instagram ads in Russia",
    "List YouTube ads in China",
    "Show ads on Facebook in South Africa",
    "Display Instagram ads in Nigeria",
    "List YouTube ads in Egypt",
    "Show ads on Facebook in Argentina",
    "Display Instagram ads in Chile",
    "List YouTube ads in Colombia",
    "Show ads on Facebook in Peru",
    "Display Instagram ads in Venezuela",
    "List YouTube ads in Saudi Arabia",
    "Show ads on Facebook in Turkey",
    "Display Instagram ads in Greece",
    "List YouTube ads in Portugal",
    "Show ads on Facebook in Sweden",
    "Display Instagram ads in Norway",
    "List YouTube ads in Finland",
    "Show ads on Facebook in Denmark",
    "Display Instagram ads in Ireland",
    "List YouTube ads in Belgium",
    "Show ads on Facebook in Switzerland",
    "Display Instagram ads in Austria",
    "List YouTube ads in Netherlands",
    "Show ads on Facebook in Poland",
    "Display Instagram ads in Czech Republic",
    "List YouTube ads in Hungary",
    "Show ads on Facebook in Slovakia",
    "Display Instagram ads in Romania",
    "List YouTube ads in Bulgaria",
    "Show ads on Facebook in Ukraine",
    "Display Instagram ads in Belarus",
    "List YouTube ads in Kazakhstan",
    "Show ads on Facebook in Uzbekistan",
    "Display Instagram ads in Turkmenistan",
    "List YouTube ads in Kyrgyzstan",
    "Show ads on Facebook in Tajikistan",
    "Display Instagram ads in Afghanistan",
    "List YouTube ads in Pakistan",
    "Show ads on Facebook in Bangladesh",
    "Display Instagram ads in Sri Lanka",
    "List YouTube ads in Nepal",
    "Show ads on Facebook in Bhutan",
    "Display Instagram ads in Maldives",
    "List YouTube ads in Myanmar",
    "Show ads on Facebook in Thailand",
    "Display Instagram ads in Vietnam",
    "List YouTube ads in Cambodia",
    "Show ads on Facebook in Laos",
    "Display Instagram ads in Malaysia",
    "List YouTube ads in Singapore",
    "Show ads on Facebook in Indonesia",
    "Display Instagram ads in Philippines",
    "List YouTube ads in Brunei",
    "Show ads on Facebook in East Timor",
    "Display Instagram ads in Papua New Guinea",
    "List YouTube ads in New Zealand",
    "Show ads on Facebook in Fiji",
    "Display Instagram ads in Solomon Islands",
    "List YouTube ads in Vanuatu",
    "Show ads on Facebook in Samoa",
    "Display Instagram ads in Tonga",
    "List YouTube ads in Tuvalu",
    "Show ads on Facebook in Nauru",
    "Display Instagram ads in Palau",
    "List YouTube ads in Micronesia",
    "Show ads on Facebook in Marshall Islands",
    "Display Instagram ads in Kiribati",
    "List YouTube ads in Maldives",
    "Show ads on Facebook in Azerbaijan",
    "Display Instagram ads in Georgia",
    "List YouTube ads in Armenia",
    "Show ads on Facebook in Lebanon",
    "Display Instagram ads in Jordan",
    "List YouTube ads in Israel",
    "Show ads on Facebook in Palestine",
    "Display Instagram ads in Syria",
    "List YouTube ads in Iraq",
    "Show ads on Facebook in Kuwait",
    "Display Instagram ads in Bahrain",
    "List YouTube ads in Qatar",
    "Show ads on Facebook in UAE",
    "Display Instagram ads in Oman",
    "List YouTube ads in Yemen",
    "Show ads on Facebook in Cyprus",
    "Display Instagram ads in Montenegro",
    "List YouTube ads in Kosovo",
    "Show ads on Facebook in Serbia",
    "Display Instagram ads in Bosnia and Herzegovina",
    "List YouTube ads in North Macedonia",
    "Show ads on Facebook in Albania",
    "Display Instagram ads in Croatia",
    "List YouTube ads in Slovenia",
    "Show ads on Facebook in Lithuania",
    "Display Instagram ads in Latvia",
    "List YouTube ads in Estonia",
    "Show ads on Facebook in Moldova",
    "Display Instagram ads in Armenia",
    "List YouTube ads in Belarus",
    "Show ads on Facebook in Iceland",
    "Display Instagram ads in Malta",
    "List YouTube ads in Luxembourg",
    "Show ads on Facebook in Liechtenstein",
    "Display Instagram ads in Monaco",
    "List YouTube ads in San Marino",
    "Show ads on Facebook in Andorra",
    "Display Instagram ads in Vatican City",
    "List YouTube ads in Lichtenstein",
    "Show ads on Facebook in San Marino",
    "Display Instagram ads in Monaco",
    "List YouTube ads in Luxembourg",
    "Show ads on Facebook in Greenland",
    "Display Instagram ads in Faroe Islands",
    "List YouTube ads in New Caledonia",
    "Show ads on Facebook in French Polynesia",
    "Display Instagram ads in Fiji",
    "List YouTube ads in Samoa",
    "Show ads on Facebook in Solomon Islands",
    "Display Instagram ads in Tonga",
    "List YouTube ads in Vanuatu",
    "Show ads on Facebook in Papua New Guinea",
    "Display Instagram ads in East Timor",
    "List YouTube ads in Brunei",
    "Show ads on Facebook in Singapore",
    "Display Instagram ads in Malaysia",
    "List YouTube ads in Myanmar",
    "Show ads on Facebook in Laos",
    "Display Instagram ads in Cambodia",
    "List YouTube ads in Vietnam",
    "Show ads on Facebook in Thailand",
    "Display Instagram ads in Bangladesh",
    "Show ads on Facebook in the United States",
    "Display Instagram ads in India",
    "List YouTube ads in the United Kingdom",
    "Show ads on Facebook in Australia",
    "Display Instagram ads in Canada",
    "List YouTube ads in Germany",
    "Show ads on Facebook in France",
    "Display Instagram ads in Japan",
    "List YouTube ads in South Korea",
    "Show ads on Facebook in Brazil",
    "Display Instagram ads in Italy",
    "List YouTube ads in Spain",
    "Show ads on Facebook in Mexico",
    "Display Instagram ads in Russia",
    "List YouTube ads in China",
    "Show ads on Facebook in South Africa",
    "Display Instagram ads in Nigeria",
    "List YouTube ads in Egypt",
    "Show ads on Facebook in Argentina",
    "Display Instagram ads in Chile",
    "List YouTube ads in Colombia",
    "Show ads on Facebook in Peru",
    "Display Instagram ads in Venezuela",
    "List YouTube ads in Saudi Arabia",
    "Show ads on Facebook in Turkey",
    "Display Instagram ads in Greece",
    "List YouTube ads in Portugal",
    "Show ads on Facebook in Sweden",
    "Display Instagram ads in Norway",
    "List YouTube ads in Finland",
    "Show ads on Facebook in Denmark",
    "Display Instagram ads in Ireland",
    "List YouTube ads in Belgium",
    "Show ads on Facebook in Switzerland",
    "Display Instagram ads in Austria",
    "List YouTube ads in Netherlands",
    "Show ads on Facebook in Poland",
    "Display Instagram ads in Czech Republic",
    "List YouTube ads in Hungary",
    "Show ads on Facebook in Slovakia",
    "Display Instagram ads in Romania",
    "List YouTube ads in Bulgaria",
    "Show ads on Facebook in Ukraine",
    "Display Instagram ads in Belarus",
    "List YouTube ads in Kazakhstan",
    "Show ads on Facebook in Uzbekistan",
    "Display Instagram ads in Pakistan",
    "List YouTube ads in Bangladesh",
    "Show ads on Facebook in Sri Lanka",
    "Display Instagram ads in Thailand",
    "List YouTube ads in Vietnam",
    "Show ads on Facebook in Malaysia",
    "Display Instagram ads in Singapore",
    "List YouTube ads in Indonesia",
    "Show ads on Facebook in Philippines",
    "Display Instagram ads in New Zealand",
    "List YouTube ads in Fiji",
    "Show ads on Facebook in Israel",
    "Display Instagram ads in Lebanon",
    "List YouTube ads in Jordan",
    "Show ads on Facebook in United Arab Emirates",
    "Display Instagram ads in Qatar",
    "List YouTube ads in Kuwait",
    "Show ads on Facebook in Oman",
    "Display Instagram ads in Bahrain",
    "List YouTube ads in Iraq",
    "Show ads on Facebook in Iran",
    "Display Instagram ads in Afghanistan",
    "List YouTube ads in Kenya",
    "Show ads on Facebook in Ethiopia",
    "Display Instagram ads in Tanzania",
    "List YouTube ads in Uganda",
    "Show ads on Facebook in Algeria",
    "Display Instagram ads in Morocco",
    "List YouTube ads in Tunisia",
    "Show ads on Facebook in Libya",
    "Display Instagram ads in Sudan",
# Combinations with the United States
    "Show Facebook ads in the United States",
    "Display Instagram ads in the United States",
    "List YouTube ads in the United States",
    "Show Facebook and Instagram ads in the United States",
    "Display Facebook and YouTube ads in the United States",
    "List Instagram and YouTube ads in the United States",
    "Show Facebook, Instagram, and YouTube ads in the United States",

    # Combinations with India
    "Show Facebook ads in India",
    "Display Instagram ads in India",
    "List YouTube ads in India",
    "Show Facebook and Instagram ads in India",
    "Display Facebook and YouTube ads in India",
    "List Instagram and YouTube ads in India",
    "Show Facebook, Instagram, and YouTube ads in India",

    # Combinations with the United Kingdom
    "Show Facebook ads in the United Kingdom",
    "Display Instagram ads in the United Kingdom",
    "List YouTube ads in the United Kingdom",
    "Show Facebook and Instagram ads in the United Kingdom",
    "Display Facebook and YouTube ads in the United Kingdom",
    "List Instagram and YouTube ads in the United Kingdom",
    "Show Facebook, Instagram, and YouTube ads in the United Kingdom",

    # Combinations with Australia
    "Show Facebook ads in Australia",
    "Display Instagram ads in Australia",
    "List YouTube ads in Australia",
    "Show Facebook and Instagram ads in Australia",
    "Display Facebook and YouTube ads in Australia",
    "List Instagram and YouTube ads in Australia",
    "Show Facebook, Instagram, and YouTube ads in Australia",

    # Combinations with Canada
    "Show Facebook ads in Canada",
    "Display Instagram ads in Canada",
    "List YouTube ads in Canada",
    "Show Facebook and Instagram ads in Canada",
    "Display Facebook and YouTube ads in Canada",
    "List Instagram and YouTube ads in Canada",
    "Show Facebook, Instagram, and YouTube ads in Canada",

    # Combinations with Germany
    "Show Facebook ads in Germany",
    "Display Instagram ads in Germany",
    "List YouTube ads in Germany",
    "Show Facebook and Instagram ads in Germany",
    "Display Facebook and YouTube ads in Germany",
    "List Instagram and YouTube ads in Germany",
    "Show Facebook, Instagram, and YouTube ads in Germany",

    # Combinations with France
    "Show Facebook ads in France",
    "Display Instagram ads in France",
    "List YouTube ads in France",
    "Show Facebook and Instagram ads in France",
    "Display Facebook and YouTube ads in France",
    "List Instagram and YouTube ads in France",
    "Show Facebook, Instagram, and YouTube ads in France",

    # Combinations with Japan
    "Show Facebook ads in Japan",
    "Display Instagram ads in Japan",
    "List YouTube ads in Japan",
    "Show Facebook and Instagram ads in Japan",
    "Display Facebook and YouTube ads in Japan",
    "List Instagram and YouTube ads in Japan",
    "Show Facebook, Instagram, and YouTube ads in Japan",

    # Combinations with South Korea
    "Show Facebook ads in South Korea",
    "Display Instagram ads in South Korea",
    "List YouTube ads in South Korea",
    "Show Facebook and Instagram ads in South Korea",
    "Display Facebook and YouTube ads in South Korea",
    "List Instagram and YouTube ads in South Korea",
    "Show Facebook, Instagram, and YouTube ads in South Korea",

    # Combinations with Brazil
    "Show Facebook ads in Brazil",
    "Display Instagram ads in Brazil",
    "List YouTube ads in Brazil",
    "Show Facebook and Instagram ads in Brazil",
    "Display Facebook and YouTube ads in Brazil",
    "List Instagram and YouTube ads in Brazil",
    "Show Facebook, Instagram, and YouTube ads in Brazil",

    # Combinations with Italy
    "Show Facebook ads in Italy",
    "Display Instagram ads in Italy",
    "List YouTube ads in Italy",
    "Show Facebook and Instagram ads in Italy",
    "Display Facebook and YouTube ads in Italy",
    "List Instagram and YouTube ads in Italy",
    "Show Facebook, Instagram, and YouTube ads in Italy",

    # Combinations with Spain
    "Show Facebook ads in Spain",
    "Display Instagram ads in Spain",
    "List YouTube ads in Spain",
    "Show Facebook and Instagram ads in Spain",
    "Display Facebook and YouTube ads in Spain",
    "List Instagram and YouTube ads in Spain",
    "Show Facebook, Instagram, and YouTube ads in Spain",

    # Combinations with Mexico
    "Show Facebook ads in Mexico",
    "Display Instagram ads in Mexico",
    "List YouTube ads in Mexico",
    "Show Facebook and Instagram ads in Mexico",
    "Display Facebook and YouTube ads in Mexico",
    "List Instagram and YouTube ads in Mexico",
    "Show Facebook, Instagram, and YouTube ads in Mexico",

    # Combinations with Russia
    "Show Facebook ads in Russia",
    "Display Instagram ads in Russia",
    "List YouTube ads in Russia",
    "Show Facebook and Instagram ads in Russia",
    "Display Facebook and YouTube ads in Russia",
    "List Instagram and YouTube ads in Russia",
    "Show Facebook, Instagram, and YouTube ads in Russia",

    # Combinations with China
    "Show Facebook ads in China",
    "Display Instagram ads in China",
    "List YouTube ads in China",
    "Show Facebook and Instagram ads in China",
    "Display Facebook and YouTube ads in China",
    "List Instagram and YouTube ads in China",
    "Show Facebook, Instagram, and YouTube ads in China",

    # Combinations with South Africa
    "Show Facebook ads in South Africa",
    "Display Instagram ads in South Africa",
    "List YouTube ads in South Africa",
    "Show Facebook and Instagram ads in South Africa",
    "Display Facebook and YouTube ads in South Africa",
    "List Instagram and YouTube ads in South Africa",
    "Show Facebook, Instagram, and YouTube ads in South Africa",

    # Combinations with Nigeria
    "Show Facebook ads in Nigeria",
    "Display Instagram ads in Nigeria",
    "List YouTube ads in Nigeria",
    "Show Facebook and Instagram ads in Nigeria",
    "Display Facebook and YouTube ads in Nigeria",
    "List Instagram and YouTube ads in Nigeria",
    "Show Facebook, Instagram, and YouTube ads in Nigeria",

    # Combinations with Egypt
    "Show Facebook ads in Egypt",
    "Display Instagram ads in Egypt",
    "List YouTube ads in Egypt",
    "Show Facebook and Instagram ads in Egypt",
    "Display Facebook and YouTube ads in Egypt",
    "List Instagram and YouTube ads in Egypt",
    "Show Facebook, Instagram, and YouTube ads in Egypt",

    # Combinations with Argentina
    "Show Facebook ads in Argentina",
    "Display Instagram ads in Argentina",
    "List YouTube ads in Argentina",
    "Show Facebook and Instagram ads in Argentina",
    "Display Facebook and YouTube ads in Argentina",
    "List Instagram and YouTube ads in Argentina",
    "Show Facebook, Instagram, and YouTube ads in Argentina"
    ]

search_list=[i.lower() for i in sample_searches]