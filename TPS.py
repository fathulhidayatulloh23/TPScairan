import streamlit as st

#navigasi sidebar
from streamlit_option_menu import option_menu

with st.sidebar:
    import streamlit as st
    from PIL import Image

    image = Image.open('Logo.PNG')
    st.image(image, caption='POLITEKNIK AKA BOGOR')
    selected = option_menu("Menu Utama", ['Nama Anggota Kelompok', 'Deskripsi Website Aplikasi', 'Perhitungan'],default_index=0)          
    

#Nama Anggota
if (selected == 'Nama Anggota Kelompok'):
    st.write('''Kelas 1E - PENJAMINAN MUTU INDUSTRI PANGAN''')
    st.write('''POLITEKNIK AKA BOGOR''')
    st.write('''Kelompok 3:
    \n1. Intan Aulia Sari             (2220458)
    \n2. Khairunnisa Mahirah          (2220460)
    \n3. Khalil Fiqih                 (2220461)
    \n4. Muhammad Fathul Hidayatulloh (2220468)
    \n5. Rifa Fauziah                 (2220484)
    ''')

if (selected == 'Deskripsi Website Aplikasi'): 
    st.title('Aplikasi Perhitungan Teknik Pengambilan Sampel')
    st.caption('Aplikasi ini digunakan dalam mempermudah perhitungan untuk menentukan titik pengambilan sampel dan banyaknya volume cairan yang diambil pada sampel cairan terkemas. Pengambilan contoh (sampling) adalah mengambil sejumlah atau sebagian bahan atau barang yang dilakukan dengan menggunakan metode tertentu sehingga bagian barang atau bahan yang diambil bersifat mewakili (representatif) terhadap keseluruhan barang atau bahan (populasi). Contoh (sampel) yang mewakili adalah suatu sampel yang diperoleh dengan menggunakan teknik sampling yang sesuai. Menurut SNI 19-0429-1989 tentang pengambilan contoh cairan dan semi padat, populasi dibedakan menjadi bahan cairan/semi padat curah dan bahan cairan/semi padat terkemas. Untuk pengambilan sampel cairan terkemas ini,  Jumlah volume contoh setiap pengambilan harus sama dan seluruh contoh dihomogenkan atau dijadikan satu contoh bahan uji. Apabila contoh dikemas dalam tangki silinder horizontal maka pengambilan contoh ditentukan oleh berapa persen tangki terisi cairan, maka volume perbandingannya itu berpacu pada tabel Penentuan Titik-Titik Pengambilan Contoh Cairan dalam Tangki berdasarkan SNI.')
    import streamlit as st
    from PIL import Image

    image = Image.open('tabel.PNG')

    st.image(image, caption='Tabel Penentuan Titik-Titik Pengambilan Contoh Cairan dalam Tangki berdasarkan SNI')
    
if (selected == 'Perhitungan'):
    st.title (':oil_drum: Menentukan Titik dan Volume Pengambilan Sampel Cairan Terkemas :oil_drum:')
    
    import streamlit as st
    from PIL import Image

    image = Image.open('tps.PNG')

    st.image(image, caption='Rumus dalam menentukan presentase tinggi cairan terhadap tinggi tangki')

    st.write('-----')

    tinggitangki=st.number_input('Masukkan tinggi tangki (cm)')
    tinggicairan=st.number_input('Masukkan tinggi cairan (cm)')
    volumesampel=st.number_input('Masukkan banyaknya volume total sampel yang harus diambil (mL)')

    if tinggicairan>tinggitangki:
        st.error('This is an error', icon="🚨")
        st.info('Masukkan tinggi tangki dan tinggi cairan yang benar', icon="ℹ️")
        st.stop()
    
    if st.button('Hitung'):
        Persen=((tinggicairan/tinggitangki)*100)
        if tinggicairan<tinggitangki:
            st.success(f'Persentase tinggi cairan terhadap tinggi tangki adalah {Persen}%')
            if Persen<10:
                st.info('Persentase tinggi cairan terhadap tinggi tangki harus di atas 10%', icon="ℹ️")
            st.write('-----')            
        st.info('HASIL TITIK PENGAMBILAN SAMPEL')         
        if Persen>=10 and Persen<=14: 
            st.success(f'Bagian atas tidak diambil')
            st.success(f'Bagian tengah tidak diambil')
            bawah=((5/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
                
        if Persen>=15 and Persen<=24: 
            st.success(f'Bagian atas tidak diambil')
            st.success(f'Bagian tengah tidak diambil')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
           
        if Persen>=25 and Persen<=34: 
            st.success(f'Bagian atas tidak diambil')
            tengah=((20/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
        
        if Persen>=35 and Persen<=44: 
            st.success(f'Bagian atas tidak diambil')
            tengah=((25/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
    
        if Persen>=45 and Persen<=54: 
            st.success(f'Bagian atas tidak diambil')
            tengah=((30/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
        
        if Persen>=55 and Persen<=64: 
            atas=((55/100)*tinggitangki)
            st.success(f'Bagian atas diambil pada titik {atas} cm')
            tengah=((35/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
        
        if Persen>=65 and Persen<=74: 
            atas=((65/100)*tinggitangki)
            st.success(f'Bagian atas diambil pada titik {atas} cm')
            tengah=((40/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
       
        if Persen>=75 and Persen<=84: 
            atas=((65/100)*tinggitangki)
            st.success(f'Bagian atas diambil pada titik {atas} cm')
            tengah=((45/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
        
        if Persen>=85 and Persen<=94: 
            atas=((85/100)*tinggitangki)
            st.success(f'Bagian atas diambil pada titik {atas} cm')
            tengah=((50/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
    
        if Persen>=95 and Persen<=100: 
            atas=((90/100)*tinggitangki)
            st.success(f'Bagian atas diambil pada titik {atas} cm')
            tengah=((50/100)*tinggitangki)
            st.success(f'Bagian tengah diambil pada titik {tengah} cm')
            bawah=((10/100)*tinggitangki)
            st.success(f'Bagian bawah diambil pada titik {bawah} cm')
            
        st.write('-----')
        st.info('HASIL VOLUME PENGAMBILAN SAMPEL') 
        if Persen>=10 and Persen<=14: 
            st.success(f'Bagian atas tidak diambil')
            st.success(f'Bagian tengah tidak diambil')
            bottom=((100/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
                
        if Persen>=15 and Persen<=24: 
            st.success(f'Bagian atas tidak diambil')
            st.success(f'Bagian tengah tidak diambil')
            bottom=((100/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
           
        if Persen>=25 and Persen<=34: 
            st.success(f'Bagian atas tidak diambil')
            middle=((60/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((40/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
        
        if Persen>=35 and Persen<=44: 
            st.success(f'Bagian atas tidak diambil')
            middle=((70/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((30/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
    
        if Persen>=45 and Persen<=54: 
            st.success(f'Bagian atas tidak diambil')
            middle=((80/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((20/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
        
        if Persen>=55 and Persen<=64: 
            top=((10/100)*volumesampel)
            st.success(f'Bagian atas diambil volume sampel sebanyak {top} mL')
            middle=((80/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((10/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
        
        if Persen>=65 and Persen<=74: 
            top=((10/100)*volumesampel)
            st.success(f'Bagian atas diambil volume sampel sebanyak {top} mL')
            middle=((30/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((10/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
       
        if Persen>=75 and Persen<=84: 
            top=((10/100)*volumesampel)
            st.success(f'Bagian atas diambil volume sampel sebanyak {top} mL')
            middle=((80/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((10/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
        
        if Persen>=85 and Persen<=94: 
            top=((10/100)*volumesampel)
            st.success(f'Bagian atas diambil volume sampel sebanyak {top} mL')
            middle=((80/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((10/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')
    
        if Persen>=95 and Persen<=100: 
            top=((10/100)*volumesampel)
            st.success(f'Bagian atas diambil volume sampel sebanyak {top} mL')
            middle=((80/100)*volumesampel)
            st.success(f'Bagian tengah diambil volume sampel sebanyak {middle} mL')
            bottom=((10/100)*volumesampel)
            st.success(f'Bagian bawah diambil volume sampel sebanyak {bottom} mL')

