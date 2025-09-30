import streamlit as st

generos = {
    'Gospel' :     {
        'Aline Barros' : 'https://youtu.be/HDMfJjhaMdE?si=mP3ESr0grm04LJXQ',
        'Fernandinho' : 'https://youtu.be/D1GDDvrfnfc?si=owSgWeaTZbaf9_78'
    },
    'Sertanejo' : {
        'Gustavo Lima' : 'https://www.youtube.com/watch?v=hEBjnXXWgKU',
        'Henrique e Juliano' : 'https://youtu.be/9Vt4XguN2-A?si=0DzKowGzUxEjM0Cm'
    },
    'Pagode' : {
        'Zeca Pagodinho' : 'https://youtu.be/Nm5N4iFLU0g?si=9cWDLScgU35v__nb',
        'Tiaguinho' : 'https://youtu.be/YnS1dQAnyTk?si=qKK3KlUJ9EqEfhla'
    },
    'Eletronica' : {
        'Alok' : 'https://youtu.be/VQ2EyU75p2o?si=jJ8O7hZNXET5MpZb',
        'Bruno Martini' : 'https://youtu.be/GeONo6C87fM?si=FFEHvhl8gpVSOcTz'
    }
}

st.sidebar.title('Sonus Playlist')
st.sidebar.image(f'logo.png')

genero = st.sidebar.selectbox('Selecione um genero musical', generos.keys())

artista = st.sidebar.selectbox('Selecione um artista', generos[genero].keys())

st.title(artista)

video, sobre = st.tabs(['Vídeo', 'Sobre o artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Aline Barros':
        st.markdown('''
            Aline Kistenmacker Barros dos Santos MT MmPE é uma cantora, compositora e pastora brasileira. Considerada uma das maiores cantoras de música cristã do Brasil, sendo certificada pela Pro-Música Brasil com vários discos de ouro, platina e diamante. Ganhou por 8 vezes o Grammy de Melhor Álbum de Música Gospel..[3]
            ''')
    
    elif artista == 'Fernandinho':
        st.markdown('''
            Fernando Jerônimo dos Santos Júnior, conhecido popularmente como Fernandinho, é um cantor brasileiro de música cristã contemporânea, compositor e pastor evangélico. Casado com Paula Santos, é pai de Asafe, Abner e Mariah..[1][2]
            ''')
        
    elif artista == 'Gustavo Lima':
        st.markdown(''' 
            Nivaldo Batista Lima (Presidente Olegário, 3 de setembro de 1989), mais conhecido pelo nome artístico Gusttavo Lima, é um cantor, compositor, produtor musical e empresário brasileiro.[2][3]

            Gusttavo Lima possui uma fortuna avaliada em mais de 1 bilhão de reais, consolidando-se como um dos artistas mais ricos do Brasil.[4][5]
            ''')
    elif artista == 'Henrique e Juliano':
        st.markdown('''
            Henrique & Juliano é uma dupla de sertanejo universitário formada pelos irmãos Ricelly Henrique Tavares Reis e Edson Alves dos Reis Junior, ambos nascidos na cidade de Palmeirópolis no interior do estado do Tocantins.
                    ''')
    elif artista == 'Zeca Pagodinho':
        st.markdown('''
            Jessé Gomes da Silva Filho, conhecido pelo nome artístico Zeca Pagodinho, é um cantor e compositor brasileiro atuante desde o final da década de 1980 e atualmente tido pela crítica e pela imprensa especializada como um dos mais exponenciais nomes do samba.
                    ''')
    elif artista == 'Tiaguinho':
        st.markdown('''
            Thiago André Barbosa, mais conhecido pelo seu nome artístico Thiaguinho, é um cantor, compositor, apresentador e empresário brasileiro.
                    ''')
    elif artista == 'Alok':
        st.markdown('''
            Alok Achkar Peres Petrillo é um DJ e produtor musical brasileiro, mais conhecido por seu sucesso mundial de 2016 "Hear Me Now". É atualmente o 4.º melhor DJ do mundo segundo a revista britânica DJ Mag.
                    ''')
    elif artista == 'Bruno Martini':
        st.markdown('''
            Bruno Dalla Martha Martini conhecido apenas como Bruno Martini é um músico, cantor, compositor, produtor, ator e DJ brasileiro. Filho de Gino Martini, integrante da banda musical Double You, ainda criança acompanhava seu pai nas produções de suas músicas e nos shows.
                    ''')

