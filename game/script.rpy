# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



init: 

    image bg warteg siang = "bg_warteg_siang.png"
    image bg warteg malam = "bg_warteg_malam.png"
    image bg bad ending = "bad_end.png"

    define siti = Character("Siti")
    image siti = im.Scale("fm02-body.png", 500 , 900)

    define ivan = Character("Ivan")
    image ivan = im.Scale("m01-body.png", 500, 900)

    define ayu = Character("Ayu")
    image ayu = im.Scale("A_1.png", 638, 900)

    define dani = Character("Dani")
    image dani = im.Scale("B_1.png", 638, 900)

    define citra = Character("Citra")
    image citra = im.Scale("fm01-body.png", 500, 900)

    define bunga = Character("Bunga")
    image bunga = im.Scale("C_1.png", 638, 900)

    python:
        import random

        day_events = ["dayEvent1", "dayEvent2", "dayEvent3", "dayEvent4"]
        good_recipes = [
            "Mie goreng + Kentang balado", 
            "Nasi + Tempe Orek + Sayur Bayam + Sambal Terasi",
            "Nasi + Telur Dadar + Sambal Kentang Hati",
            "Nasi + Ayam Goreng + Sayur Asem + Tempe Orek",
            "Nasi + Telur Balado + Kol Goreng",
            "Nasi + Ayam Semur + Perkedel + Sambal Ijo"
        ]
        bad_recipes = [
            "Nasi + Semangka",
            "Nasi + Sayur Asem + Soto Kuah Dicampur",
            "Nasi + Sambal 3 Jenis",
            "Nasi + Ikan Asin + Kol Goreng + Es Teh Manis dicampur jadi kuah nasi",
            "Nasi + Soto Kuah + Mie Goreng + Sambal"
        ]
        month = 1
        week = 1
        year = 1
        reputation = 1.0
        money = 1000000
        income = 500000
        wages = 1200000
        expenses = 300000
        
screen time ():
    frame:
        align (0, 0)
        has vbox
        text "Tahun : [year]" align (0.0, 0.0)
        text "Bulan : [month]" align (0.0, 0.0)
        text "Minggu : [week]" align (0.0, 0.0)

screen money ():
    frame:
        align (1.0, 0.0)
        has vbox
        text "Uang : Rp [money]" align (1.0, 0.0)


# The game starts here.

label start:
    play music "6-Happy-Commercial-Piano.mp3"
    scene bg warteg siang

    show siti
    siti "Halo selamat siang"
    siti "Kamu ya pemilik baru warteg ini"
    siti "Masih muda tapi sudah punya usaha, kamu hebat ya"
    siti "Jadi, aku bisa panggil kamu apa?"

    $ player = renpy.input("Namaku siapa ya?").strip()
    
    if player:
        siti "[player]..."
        siti "Nama yang bagus! Senang bertemu denganmu"
        siti "Aku akan coba sebaik mungkin untuk membantumu mengelola warteg ini"
    else:
        siti "Hmmm....Gak mau kasih tahu nama \nKamu mau jadi sok misterius ya?"
        siti "Yaudah aku panggil kamu Budi saja biar gampang"
        $ player = "Budi"
        siti "Mohon bantuannya ya [player]!"

    player "Ya senang bertemu denganmu"
    player "Oh iya aku belum tahu namamu"

    siti "Astaga!"
    siti "Aku sampai lupa memperkenalkan diri"
    siti "Namaku Siti, kamu bisa panggil aku jika butuh bantuan"

    jump day1

    return


label day1:
    scene bg warteg siang with fade
    
    player "Saatnya buka warteg!!\nAyo semangat!!!"
    player "Tapi apa saja yang perlu dilakukuan ya?"
    player "Sebentar aku panggil Siti dulu"

    show siti
    siti "Kau mau tahu apa saja yang harus dilakukan?"
    siti "Baiklah sepertinya kamu butuh pelatihan spesial dariku"

    show screen time ()

    siti "Di sebelah kiri atas adalah penanda waktu saat ini"
    siti "Sedikit saran saja dariku, jangan lupa untuk mengecek waktu saat ini"
    siti "Jangan sampai kamu terlena karena terlalu fokus"

    show screen money ()

    siti "Di sebelah kanan atas ada jumlah uang yang kamu miliki saat ini"
    siti "Uang adalah sumber daya yang penting, gunakan sebaik mungkin untuk membantu bisnis wartegmu"
    siti "Setiap minggu jumlah uangmu akan diperbarui sesuai dengan pendapatan warteg"
    siti "Uang belanja bahan kebutuhan warteg setiap minggu akan mengurangi jumlah uangmu"
    siti "Jangan lupa juga setiap akhir bulan kamu harus menggaji pegawai warteg"
    siti "Saat ini memang hanya ada aku, tapi jangan kira tenagaku harganya murah lho hehehe"
    siti "Hati-hati agar tidak menggunakan uang sembarangan \nJika uangmu habis maka kamu tidak bisa melanjutkan bisnis warteg dan bankrut"

    siti "Di siang hari, seharusnya tidak banyak yang harus kamu lakukan \nSemuanya akan aku coba tangani"
    siti "Tapi kadang warteg akan ramai jadi aku minta bantuanmu untuk melayani pelanggan"
    siti "Hati-hati saat menangani pelanggan, pelayanan yang buruk dapat mengurangi reputasi warteg"
    siti "Di malam hari, kamu bisa coba bereksperimen untuk meningkatkan cita rasa menu di warteg"
    siti "Jika menu-nya semakin lezat, tentu saja akan semakin banyak pengunjung yang datang dan makan di warteg"

    hide siti

    "Pelanggan mulai datang dan warteg menjadi sibuk"

    show ivan
    ivan "Mas! Pesan yang biasa ya makan disini"
    player "Eh? Yang biasa itu maksudnya apa ya mas?"
    ivan "Ya yang biasa Mas.... \nLoh?"
    ivan "Mas pegawai baru ya? Belum pernah lihat aku"
    player "Haha iya mas"
    ivan "Yaudah aku pesan nasi, telor balado, sama sayur singkong ya makan disini"
    player "Siapp"
    player "(Ohhh sepertinya itu menu yang selalu dia pesan disini)"
    player "(Sebaiknya aku coba ingat-ingat menu pelanggan setia warteg)"

    scene black with fade
    
label night1:
    scene bg warteg malam with fade

    player "huft lumayan capek juga ya"
    
    show siti
    siti "Kerja bagus... Hari ini warteg-nya lumayan ramai ya"
    siti "Hari ini pendapatan warteg Rp [income]. Tidak buruk untuk hari pertama"

    play sound "money-counting.mp3"
    $ money = money + income

    siti "Jangan lupa mulai besok kamu harus mulai belanja untuk kebutuhan warteg ya"
    siti "Karena sudah malam aku mau pulang dulu \nKamu bisa coba-coba modifikasi menu tapi jangan lupa istirahat ya"

    hide siti with fade

    player "Hmmmm....Siti sudah pulang \nSebaiknya aku ngapain ya?"
    menu:
        "Mau apa malam ini?" 

        "Istirahat":
            player "Ah aku capek. Langsung tidur aja lah biar besok semangat kerja di warteg"
        "Kembangkan menu warteg":
            player "Saatnya menunjukkan cita rasaku ke dunia!"
            "Aku menambahkan asal beberapa bumbu dan rempah yang warnanya cerah ke telur dadar"
            
            play sound "playful-failure.mp3"
            player "Waduh eksperimennya gagal"
            
            $ reputation -= 0.02 
            
            player "HUEKK kok rasanya jadi begini sih?!!"
            player "Duh kalau begini bisa-bisa tidak ada pelanggan yang datang karena rasa makanan tidak enak"
            player "Aku harus mulai belajar memasak dengan benar biar makanannya gak gagal seperti malam ini!"
    jump dayEvent



label dayEvent:
    scene bg warteg siang

    play sound "money-counting.mp3"
    player "Hmmm... total pengeluaran untuk kebutuhan warteg ini adalah Rp [expenses]"
    $ money = money - expenses


    if money < 0:
        player "Waduh, uangku gak cukup buat belanja hari ini"
        player "Gakpapalah ngutang dulu nanti kubayar pakai keuntungan hari ini"

    player "Ayo ayo semangat kerja!!!"

    "Warteg dibuka dan pelanggan mulai berdatangan"

    $ today_event = renpy.random.choice(day_events)
    $ renpy.jump(today_event)

    with fade
    jump nightEvent 


label nightEvent:
    scene bg warteg malam
    show siti

    siti "Kerja bagus\nHari ini juga pelanggan puas"
    $ today_income = int(income*reputation)
    play sound "money-counting.mp3"
    siti "Pendapatan warteg hari ini adalah Rp [today_income]"
    $ money = money + today_income

    if week == 4:
        siti "Oh iya karena ini akhir bulan kamu harus bayar gajiku sebesar Rp [int(wages)]"
        player "Oh iya benar juga\nNih..."
        play sound "money-counting.mp3"
        player "Terima kasih atas kerja kerasnya bulan ini"
        $ money = money - int(wages)

    if money < 0:
        siti "Loh ada apa?\nKok mukamu kelihatan murung?"
        play music "Downpour.mp3"
        player "Maaf, Siti. Sepertinya mulai besok kamu tidak usah kerja di sini lagi"
        player "Aku sudah tidak punya uang lagi untuk melanjutkan warteg"
        player "Besok aku akan mulai mencari orang yang mau membeli usaha warteg ini"
        siti "Oh begitu ya..."
        siti "Sayang sekali..."
        siti "Aku tahu ini memang terasa singkat, tapi aku menikmati waktu kita bekerja bersama"
        siti "Terima kasih [player]\nAku berharap yang terbaik untuk kita semua"

        "Siti hanya dapat tersenyum simpul kepadaku\nSetelah selesai beberes dia pergi meninggalkan warteg"

        jump badEnding


    
    siti "Apa malam ini kamu mau eksperimen menu?"
    siti "Jangan lupa istirahat ya!\nBesok kita harus kerja lagi dengan penuh semangat"

    "Siti pergi meninggalkan warteg"
    hide siti with fade

    menu:
        "Mau apa malam ini?" 

        "Istirahat":
            player "Ah aku capek. Langsung tidur aja lah biar besok semangat kerja di warteg"
        "Kembangkan menu warteg":
            player "Saatnya menunjukkan cita rasaku ke dunia!"
            $ good_recipe = renpy.random.choice(good_recipes)
            $ bad_recipe = renpy.random.choice(bad_recipes)
            menu:
                "Menu kali ini adalah...."
                "[good_recipe]":
                    play sound "success-fanfare.mp3"
                    player "Hm! Rasanya lumayan juga!"
                    player "Hahaha aku benar-benar koki jenius!"
                    player "Para pelanggan pasti suka dengan menu ini!"

                    $ reputation += 0.05
                    $ wages += 0.01

                "[bad_recipe]":
                    play sound "playful-failure.mp3"
                    player "Hmm rasanya kok agak...."
                    player "Mungkin ini memang bakat tersembunyi yang lebih baik tetap disembunyikan"

                    $ reputation -= 0.02

            player "Hari ini cukup segini dulu"
            player "saatnya istirahat..."




                

    python:
        if week < 4:
            week += 1
        else:
            week = 1
            if month < 12:
                month += 1
            else:
                month = 1
                year += 1
    with fade
    jump dayEvent 



    
label dayEvent1:
    scene bg warteg siang with fade

    "Tiba-tiba aku dengar suara gaduh di warteg"

    show ivan at left
    show dani at right

    ivan "Lha gaboleh gitu mas!\nWong aku yang sampai duluan kok"
    dani "Hah gimana mas?!\nJelas-jelas aku yang datang duluan!\nGimana sih!"

    hide ivan
    show siti at left
    siti "A- aduh gimana ini?"
    player "Ada apa, Siti?\n"
    siti "Anu, [player]...\nMereka berdua mau makan tapi nasinya sisa satu porsi"
    siti "Mereka gak ada yang mau ngalah dan nunggu nasi matang lagi"

    hide siti
    show ivan at left

    menu:
        "Harus apa ya?"

        "Coba tenangkan keadaan":
            player "Aduh gimana ya?"
            player "Mas Ivan udah laper banget ya? Gimana kalau ganjal perut dulu pakai gorengan"
            player "Aku kasih gratis deh karena mas Ivan mau sabar nunggu nasi mateng"
            player "Ntar telor balado nya juga aku tambah 1 lagi"
            ivan "Wah beneran nih?!\nHehe kalo gini mah sampe besok juga sabar nih aku nungguin nasi mateng"

            "Huft untungnya mas Ivan udah langganan disini\nJadi gampang bujuknya"

            $ reputation += 0.005

            "Sepertinya reputasi warteg meningkat..."
        "Harus sama-sama adil!":
            player "Hadeh mau gimana lagi"
            player "Karena ga ada yang mau ngalah...."
            player "BIAR AKU AJA YANG DAPAT NASINYA HAHAHAHAHAHHAH"

            show ivan at center
            show siti at left
            "Siti, Ivan dan Dani tidak dapat berkata-kata dan hanya mampu melihat"

            $ reputation -= 0.05

            "Sudah pasti reputasi warteg berkurang..."

    jump nightEvent

label dayEvent2:
    scene bg warteg siang

    show citra
    citra "Halo mas\nAku mau pesan nasi, telur dadar sama sayur labu ya"
    player "Siap mbak!\nMau makan disini atau bungkus"
    citra "Makan disini mas"
    citra "Oh iya kasih sambal yang banyak ya mas!"
    player "Aduh yakin mbak?\n Khusus hari ini sambelnya super pedas loh"
    citra "Loh mas ngeremehin saya?\nUdah gausah banyak cincong langsung siapin aja"
    citra "Sambelnya kasih segayung sekalian!"
    player "waduh iya mbak segera saya siapkan"

    with fade

    citra "aduh pedes banget!!! hah.... hah...."
    "Aku melihat Citra kepedasan sampai mukanya merah dan hampir sesak nafas"

    menu:
        "Sebaiknya apa yang kulakukan"

        "Tawarin teh":
            player "Duhh...udah saya bilang sambel hari ini tuh pedes banget mbak"
            player "Nih diminum dulu tehnya"
            "Citra langsung meneguk teh yang kusodorkan"
            player "Gimana mbak? Udah mendingan?"
            citra "Udah mas\nMaaf ya mas tadi gak percaya waktu mas bilang sambelnya pedes banget"
            player "Hahaha aman aja mbak"

            "Harusnya sih reputasi warteg meningkat"
        "Pura-pura gak lihat":
            "Aku tertawa dalam hati melihat Citra gelagapan seperti ikan kehabisan nafas"

            "Loh gara-gara ini reputasi warteg turun juga??"

    jump nightEvent


label dayEvent3:
    scene bg warteg siang with fade

    show ivan
    ivan "Hah...emang sayur singkong gak ada lawan!"
    ivan "Hup saatnya kembali bekerja!"
    ivan "Jadi berapa mas?"
    player "Seperti biasa Rp 16000 mas"
    ivan "Hmmm...sip...sip\nEh? Loh?"
    ivan "Hmm anu mas dompet saya kayaknya ketinggalan...hehehe"
    ivan "Saya ngutang lagi gapapa ya mas?\nJanji besok bakal saya bayar!"
    "Aduh mas Ivan mau ngutang lagi...\nYang sebelum-sebelumnya juga belum dibayar"

    menu:
        "Gimana ya?"

        "Ga Boleh! Kali ini harus tegas!":
            player "Gaboleh mas! Yang kemarin-kemarin juga belum lunas!"
            player "Udah mau nambah utang aja"
            ivan "(Waduh kayaknya [player] bener-bener marah kali ini)"
            ivan "Eh aduh maaf mas ini ternyata ada uang cukup kok di kantong"
            ivan "Nih mas buat makan hari ini\nMakasih ya mas"
            "Ivan buru-buru pergi meninggalkan warteg"
            player "Utang yang kemarin gimana mas?!!!"
            ivan "Hehe besok pasti saya bayar mas"
            hide ivan with fade

            "Huft untung dia gak ngutang lagi hari ini"
            "Tapi besok harus kutagih sampai lunas!"

            $ reputation += 0.005
        "Apa boleh buat deh":
            player "Hahh yaudah deh"
            player "Tapi besok jangan lupa bayar ya mas!"
            ivan "Hehe siap maskuh"
            
            hide ivan with fade
            player "Hahhh"
            "Aku cuma bisa menghela nafas karena aku tahu besok Ivan pasti pura-pura lupa"

            play sound "money-counting.mp3"
            $ money -= 16000

    jump nightEvent

label dayEvent4:
    scene bg warteg siang with fade
    show bunga at left
    show siti at right

    player "Hmmm?"
    "Warteg sedang tidak terlalu ramai dan aku lihat Siti sedang mendengarkan pelanggan"
    "Tapi wajah Siti seperti tidak nyaman\nAku jadi penasaran apa yang sebenarnya terjadi"

    player "Halo mbak aku lihat dari tadi gelasnya udah kosong"
    player "Mau mesan minum dulu gak biar ngobrol nya makin betah"
    "Seketika aku lihat wajah Siti menjadi lega melihat kedatanganku"
    siti "Wah pas banget nih, [player] ini tuh berpengalaman banget!!"
    "Hmm?"
    siti "Aku yakin dia pasti bisa bantu masalah Bunga"
    "Hmmmm??????"
    bunga "Yang benar???! Dengerin deh mas [player]! Bunga tuh lagi kesel banget tauuu"
    "Seketika Siti langsung kabur meninggalkan aku yang masih kebingungan"
    hide siti show bunga with fade

    siti "Terus dengerin deh!! Si anu itu ya emang nyebelin banget tauuu!!!"
    "Sudah berapa lama aku disini?"
    "Aku bukan cuma mengenal Bunga...."
    "Aku bahkan sampai tahu silsilah keluarga musuh tetangga gebetannya dia"

    menu:
        "Apa yang harus aku lakukan?"

        "Menyerah":
            "Aku mengibarkan bendera putih, kembali ke dapur, meminta Siti membungkuskan nasi ayam dan memberikannya ke Bunga agar dia segera pulang"

            $ money -= 20000

            "Siti hanya bisa menatap kasihan ke arahku"

        "Tahan...tinggal sedikit lagi....":
            "Dia terus bercerita....lalu bercerita.....\nterus bercerita....."
            "Hah?? Sudah berapa jam yang berlalu???"
            "Saat aku sadar aku sudah ada di ranjang rumah sakit akibat kekurangan nutrisi"
            "....Bunga bercerita sebulan penuh tanpa istirahat"

            python:
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                money -= int(wages)
        
    jump nightEvent


label badEnding:
    scene bg bad ending with fade

    pause

    return
    
    
