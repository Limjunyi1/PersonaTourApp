# This file is for statics for pages/functions


def home_statics():
  # Statics (Photos and Hyperlinks)
  link1 = [
      "Tour in Akihabara", "https://www.youtube.com/watch?v=UDn2emsfJFA",
      "https://i.ytimg.com/vi/UDn2emsfJFA/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAkm4kaEI5Sp1J0_L0gp2uwphLgWQ"
  ]
  link2 = [
      "Tour in Ginza",
      "https://www.youtube.com/watch?v=dwz3Bqiwq4Y&pp=ygUNdG91ciBpbiBnaW56YQ%3D%3D",
      "https://i.ytimg.com/vi/dwz3Bqiwq4Y/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCWGHFs5ugbIaBr3wm8xoF37IOfuA"
  ]
  link3 = [
      "Tour of Nintendo World",
      "https://www.youtube.com/watch?v=m5l0N2vUEK4&pp=ygUVdG91ciBpbiBuaW50ZW5kbyBsYW5k",
      "https://i.ytimg.com/vi/m5l0N2vUEK4/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCY6G33XrQZ6cHtBCjTSfeZnri1cg"
  ]
  link4 = [
      "Tour in Akihabara", "https://www.youtube.com/watch?v=UDn2emsfJFA",
      "https://www.japan-guide.com/g18/3003_01.jpg"
  ]
  link5 = [
      "Tour in Ginza",
      "https://www.youtube.com/watch?v=dwz3Bqiwq4Y&pp=ygUNdG91ciBpbiBnaW56YQ%3D%3D",
      "https://www.japan-guide.com/g18/3005_02.jpg"
  ]
  link6 = [
      "Tour of Nintendo World",
      "https://www.youtube.com/watch?v=m5l0N2vUEK4&pp=ygUVdG91ciBpbiBuaW50ZW5kbyBsYW5k",
      "https://www.japan-guide.com/g18/3038_02.jpg"
  ]

  links = [link1, link2, link3]
  links2 = [link4, link5, link6]

  # HTML and CSS
  html_code = """
  <div class="cards">
    <div class="card" style="background-image: url('https://ichef.bbci.co.uk/news/976/cpsprodpb/0E7F/production/_128311730_gettyimages-1265028360-1.jpg');">
      <h2><a href="https://chat.openai.com/?q=Suggest a pet friendly itinerary in the city with the most pets in japan. Make it a week long with activities you can do with your pets. Give a description for each location.">Travel with pets</a></h2>
    </div>
    <div class="card" style="background-image: url('https://images.healthshots.com/healthshots/en/uploads/2022/08/28211655/romance-1600x900.jpg');">
      <h2><a href="https://chat.openai.com/?q=Suggest the most romantic itinerary in the most romantic city in japan. Make it a week long with the most romantic restaurants and couple spots. Give a description for each location.Make it extensive and clear">Feel the love</a></h2>
    </div>
    <div class="card" style="background-image: url('https://www.parents.com/thmb/6gMhztGhYdCYdjwpYotHUb_Cjnw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/shutterstock_583803574-e7537da4a36b463eb4ae472cbc7aa6c3.jpg');">
      <h2><a href="https://chat.openai.com/?q=Suggest a children friendly itinerary in the most kids friendly city in japan. Make it a week long with activitives parents can do with small children. Give a description for each location.Make it extensive and clear">Travel with kids</a></h2>
    </div>
    <div class="card" style="background-image: url('https://images.squarespace-cdn.com/content/v1/560dbc25e4b0969564758eb5/89f97555-eddb-4329-b317-5774cbbe0c8f/Akihabara-Wal-+with-Maid-Anime.jpg');">
      <h2><a href="https://chat.openai.com/?q=Suggest an anime related itinerary in the most anime like city in japan. Make it a week long with many anime related attractions. Give a description for each location.Make it extensive and clear">Anime</a></h2>
    </div>
    <div class="card" style="background-image: url('https://hips.hearstapps.com/hmg-prod/images/nature-quotes-landscape-1648265299.jpg');">
      <h2><a href="https://chat.openai.com/?q=Suggest a nature itinerary in the most nature filled city in japan. Make it a week long with many beautiful sights. Give a description for each location.Make it extensive and clear">Nature</a></h2>
    </div>
  </div>
  """

  css_code = """
  <style>
  body {
    margin: 0;
    height: 100vh;
    display: grid;
    place-items: center;
    background: #000;
    overflow: hidden;
  }
  .cards {
    display: flex;
    gap: 2rem;
    justify-content: center;
  }
  .card {
    background-size: cover;
    background-position: center;
    border-radius: 1rem;
    padding: 1rem;
    box-shadow: 3px 3px 12px 2px rgba(0, 0, 0, 0.6);
    transition: 0.2s;
    text-align: center;
    color: white;
    position: relative;
    flex: 1;
    width: 350px;
    max-width: 100%;
    font-weight: bold;
  }
  .card h2, .card p {
    position: relative;
    z-index: 2;
    color: white;
    font-size: 18px;
  }
  .card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 1rem;
    z-index: 1;
  }
  .card:hover,
  .card:focus-within {
    transform: translateY(-1rem);
  }
  </style>
  """

  return links, links2, html_code, css_code
