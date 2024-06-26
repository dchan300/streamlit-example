import streamlit as st

st.title('MongoDB Atlas Keyword-/Semantic-/Hybrid-Search Demo')


def display_results(results):
    st.write('Search results:')
    cols = st.columns(2)

    for k, m in enumerate(results):
        image_id = m.id
        image_url = 'https://open-images-dataset.s3.amazonaws.com/' + image_id

        col_id = 0 if k % 2 == 0 else 1

        with cols[col_id]:
            score = m.scores['cosine'].value
            similarity = 1 - score
            st.markdown(f'Top: [{k + 1}] Similarity: ({similarity:.3f}) {image_id}')
            print(image_url)
            cols[col_id].image(image_url)

    # data = [[r.text, st.image(), r.scores['cosine'].value] for r in results]
    # df = pd.DataFrame(
    # data,
    # columns=('caption', 'uri', 'score'))

    # st.table(df)


def search(query_da):
    res = client.post('/search', query_da)
    # for item in res[0].matches:
    #     print(item.id, item.uri)
    result = res[0].matches[:10]
    display_results(result)


menu = ['Keyword-Search', 'Semantic-Search']
choice = st.sidebar.selectbox('Select The Input Modality: ', menu)

if choice == 'Keyword-Search':
    st.subheader('Keyword-Search')
    query = st.text_input('Text Query', placeholder='Type your query here...')

    query_da = query

elif choice == 'Semantic-Search':
    st.subheader('Semantic-Search')
    query = st.text_input('Text Query', placeholder='Type your query here...')

    query_da = query

if st.button('search'):
    message = 'Wait for it...'

    with st.spinner(message):
        search(query_da)
