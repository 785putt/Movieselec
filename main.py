from bs4 import BeautifulSoup
import streamlit as st
import requests
import itertools
import random

moodslct = open('categorymd')  # opening mood select file
mooods = list(moodslct)  # turn them into a list to loop through
url = ''


def movie_imgpos():
    """Scrapping necessarily information for movie list"""

    # url = 'https://www.imdb.com/list/ls021686578/?page=2'
    # request allow you to send HTTP request
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')  # main scraping

    movie_data = soup.findAll('div', attrs={'class': 'lister-item mode-detail'})  # find movie data details
    movie_dat = soup.find_all('img', class_='loadlate')  # scrap all images
    movied = soup.find_all('div', attrs={'class': 'lister-item-image ribbonize'})  # length of movies in given list

    Name = []
    img = []
    year = []
    time = []
    rating = []
    votes = []
    description = []

    # storing movie images & names in variables #
    for mem in range(len(movied)):
        img.append(movie_dat[mem]["loadlate"])
        Name.append(movie_dat[mem]["alt"])

    # for loop to loop through every data section
    for store in movie_data:
        # release film year
        year_of_release = store.h3.find('span', class_='lister-item-year text-muted unbold').text.replace('(', '').replace(')', '')
        year.append(year_of_release)

        # runtime of the film
        runtime = store.p.find('span', class_='runtime').text  # .text.replace(' min', '')
        time.append(runtime)

        # audience rating
        rate = store.find('div', class_='ipl-rating-star small').text.replace('\n', '')
        rating.append(rate)

        value = store.find_all('span', attrs={'name': 'nv'})
        # audience vote
        vote = value[0].text
        votes.append(vote)

        describe = store.find_all('p', class_="")  # find_all('p', class_= '$0)
        # description_ = describe[1].text.replace('\n', '') if len(describe) >1 else '*****'
        describe = describe[0].text.replace('\n', '')
        description.append(describe)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Randomizing order code section

    m_in = [[a, b, c, d, e, f, g] for [a, b, c, d, e, f, g] in
            itertools.zip_longest(Name, img, year, time, rating, votes, description, fillvalue='')]
    # randomizing the order respectively
    random.shuffle(m_in)
    Name, img, year, time, rating, votes, description = itertools.zip_longest(*m_in)

    # -----------------------------------------------------------------------------------------------------------------------------
    # Displaying movies+data onto current working stream-lit webpage

    # 5 Columns component breakdown (What you see on the display)
    st.markdown("""<hr style="height:4px;border:none;color:#71808E;background-color:#71808E;" /> """, unsafe_allow_html=True)

    with st.container():        # FIRST
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(Name[4], unsafe_allow_html=True)
            st.image(img[4], caption='⭐ ' + rating[4], width=230)
        with c2:
            ''''''
        with c3:
            st.markdown('**Year of Release**')
            st.text(year[4])
            st.markdown('#')
            ''''''
            st.markdown('**Run-time**')
            st.text(time[4])
            st.markdown('#')
            ''''''
            st.markdown('**Votes**')
            st.text(votes[4])
        with c4:
            st.markdown("**Description**")
            with st.expander('See description'):
                st.write(description[4])

    st.markdown('##')
    st.markdown("""<hr style="height:4px;border:none;color:#71808E;background-color:#71808E;" /> """, unsafe_allow_html=True)

    with st.container():        # SECOND
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(Name[5], unsafe_allow_html=True)
            st.image(img[5], caption='⭐ ' + rating[5], width=230)
        with c2:
            ''''''
        with c3:
            st.markdown('**Year of Release**')
            st.text(year[5])
            st.markdown('#')
            ''''''
            st.markdown('**Run-time**')
            st.text(time[5])
            st.markdown('#')
            ''''''
            st.markdown('**Votes**')
            st.text(votes[5])
        with c4:
            st.markdown("**Description**")
            with st.expander('See description'):
                st.write(description[5])

    st.markdown('##')
    st.markdown("""<hr style="height:4px;border:none;color:#71808E;background-color:#71808E;" /> """, unsafe_allow_html=True)

    with st.container():        # THIRD
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(Name[6], unsafe_allow_html=True)
            st.image(img[6], caption='⭐ ' + rating[6], width=230)
        with c2:
            ''''''
        with c3:
            st.markdown('**Year of Release**')
            st.text(year[6])
            st.markdown('#')
            ''''''
            st.markdown('**Run-time**')
            st.text(time[6])
            st.markdown('#')
            ''''''
            st.markdown('**Votes**')
            st.text(votes[6])
        with c4:
            st.markdown("**Description**")
            with st.expander('See description'):
                st.write(description[6])

    st.markdown('##')
    st.markdown("""<hr style="height:4px;border:none;color:#71808E;background-color:#71808E;" /> """, unsafe_allow_html=True)

    with st.container():        # FOURTH
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(Name[8], unsafe_allow_html=True)
            st.image(img[8], caption='⭐ ' + rating[8], width=230)
        with c2:
            ''''''
        with c3:
            st.markdown('**Year of Release**')
            st.text(year[8])
            st.markdown('#')
            ''''''
            st.markdown('**Run-time**')
            st.text(time[8])
            st.markdown('#')
            ''''''
            st.markdown('**Votes**')
            st.text(votes[8])
        with c4:
            st.markdown("**Description**")
            with st.expander('See description'):
                st.write(description[8])

    st.markdown('##')
    st.markdown("""<hr style="height:4px;border:none;color:#71808E;background-color:#71808E;" /> """, unsafe_allow_html=True)

    with st.container():        # FIFTH
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(Name[9], unsafe_allow_html=True)
            st.image(img[9], caption='⭐ ' + rating[9], width=230)
        with c2:
            ''''''
        with c3:
            st.markdown('**Year of Release**')
            st.text(year[9])
            st.markdown('#')
            ''''''
            st.markdown('**Run-time**')
            st.text(time[9])
            st.markdown('#')
            ''''''
            st.markdown('**Votes**')
            st.text(votes[9])
        with c4:
            st.markdown("**Description**")
            with st.expander('See description'):
                st.write(description[9])

    st.markdown('##')
    st.markdown("""<hr style="height:4px;border:none;color:#71808E;background-color:#71808E;" /> """, unsafe_allow_html=True)

    with st.container():        # SIXTH
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(Name[10], unsafe_allow_html=True)
            st.image(img[10], caption='⭐ ' + rating[10], width=230)
        with c2:
            ''''''
        with c3:
            st.markdown('**Year of Release**')
            st.text(year[10])
            st.markdown('#')
            ''''''
            st.markdown('**Run-time**')
            st.text(time[10])
            st.markdown('#')
            ''''''
            st.markdown('**Votes**')
            st.text(votes[10])
        with c4:
            st.markdown("**Description**")
            with st.expander('See description'):
                st.write(description[10])

# ---------------------------------------------------------------------------------------------------------------------------------------
# --------------------------Main Menu page / expansion to navigation bar-----------------------------------------------------------------


step_ = st.sidebar.radio("Navigation", ["Home", "About this"])      # radio yield in two circle box to pick: home page or about this info page
# 1st option: movie recommender system

if step_ == "Home":
    # --Launch recommender page application   &   Title of this app itself
    st.markdown(
        "<h1 title style='font-family:tahoma; color:#FFD700; font-weight: 550; font-size: 60px; text-transform: uppercase; text-align:center;'>Movie suggestions by mood</h1>",
        unsafe_allow_html=True)     # Giant title
    ''''''
    n_ame = st.selectbox("What do you feel like?", mooods)      # Selecting menu bar

    if st.button("Recommend / Refresh"):    # condition run once button is click
        st.markdown('#')
        if 'INTENSE' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls021686578/?page=2'
            st.markdown('<h2 style="font-family:times new roman; color:#ED2A30;">List of action movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'DRAMA' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls096880821/'
            st.markdown('<h2 style="font-family:times new roman; color:#3D512E;">List of drama movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'HEROIC' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls027328830/'
            st.markdown('<h2 style="font-family:times new roman; color:#FF5733;">List of heroes movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'SUSPENSEFUL' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls021478197/'
            st.markdown('<h2 style="font-family:times new roman; color:#795F9C;">List of thriller movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'SAD' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls069504270/'
            st.markdown('<h2 style="font-family:times new roman; color:#067ED2;">List of sad movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'ROMANTIC' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls021389931/'
            st.markdown('<h2 style="font-family:times new roman; color:#D66574;">List of romantic movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'CHALLENGING' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls027345204/?ref_=otl_4'
            st.markdown('<h2 style="font-family:times new roman; color:#F8ED62;">List of intellectual movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'LIGHT-HEARTED' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls089519405/?ref_=otl_4'
            st.markdown('<h2 style="font-family:times new roman; color:#C551F6;">List of animation movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'ODD' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls009668187/'
            st.markdown('<h2 style="font-family:times new roman; color:#EAE5DB;">List of musical movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'FRIGHT' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls079318228/'
            st.markdown('<h2 style="font-family:times new roman; color:#405D65;">List of scary movies</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'SURPRISE' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls021348659/'
            st.markdown('<h2 style="font-family:times new roman; color:#C0FF00;">List of movies with turning point</h2>', unsafe_allow_html=True)
            movie_imgpos()
        if 'HISTORICAL' in n_ame.upper():
            url += 'https://www.imdb.com/list/ls009668171/'
            st.markdown('<h2 style="font-family:times new roman; color:#D4A47C;">List of noir/western movies</h2>', unsafe_allow_html=True)
            movie_imgpos()

# Sidebar page (for "Home" section)
    s_dy = st.sidebar
    with s_dy:

        st.markdown('____')
        st.markdown('For quick guide, go to section __*About this*__')

# 2nd option: about this (brief information about & how to use this app)
if step_ == "About this":
    st.markdown('<h1 style="font-family:nexa; color:#8297b3; font-size: 46px; text-decoration: underline solid">About this web application</h1>',
                unsafe_allow_html=True)
    ''' '''
    st.write("""
    Movie recommender mood-based provide plenty of movie genres for users to choose accordingly, based on current 
    feeling, with no cost of endless searching. Mood-based selectors 
    display menu options of each existing mood in the human spectrum. All one has to do is to click on the mood bar 
    within the menu bar and wait around eight seconds, then movies in a neatly laid-out list will pop out and the user 
    can go through each film for its general information. Users can choose to further their interest by looking up a 
    particular movie on the internet. If users want more movies from the same genre, then they can hit the refresh button 
    to reload, for each movie that listed out was randomized to ensure that each search does not yield the same results.\n 
    To use this recommendation system, use the provided URL link and enter it on the search bar. The web will open to the 
    main page as a first thing, where a big title, select box, and refresher button will appear on sight. A triple bar icon 
    appears on the top right corner of the page, and there are settings, theme altering mode, screen record, and bug reporting 
    buttons, as well as a directory link to the streamlit official page. 
    """)
    st.markdown('#')
    st.markdown('<h5 style="font-family:georgia, serif; color:#8297b3; font-size: 36px">How to use this app</h5>',
                unsafe_allow_html=True)
    st.write('1.  On new page, enter website URL.')
    st.write('2.  Navigation bar may appear on the left. If not then click the navigation arrow __\'>\'__ at top left corner.')
    st.write('3.  Options will be display. Choose either one to explore. ')
    st.write('4.  Once loaded, click on an central empty bar to select mood (drop bar will appear).')
    st.markdown('5.  Click __Recommend/Refresh__ button below. Wait for few seconds.')
    st.write('6.  Enjoy your selection!')
    st.markdown('7.  Click on refresh button to reload new movie, or click on navigation arrow to explore again.')
# Sidebar page (for "About this" section)
    st.sidebar.markdown('____')
    st.sidebar.markdown('__*NOTE*__: this web application is made by Puttipong Aunggulsant, CIE first year student, made for _non commercial_ uses.')
