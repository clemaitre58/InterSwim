Script pour générer les inter de nage pour série à la PMA à partir d'un temps au 400m.

Il possible de générer une plage complète pour voir l'évoluation des inter en fonction des temps au 400.

Exemple d'usage:


    T_deb_sim = Time(8, 00)
    T_fin_sim = Time(5, 45)

    allure_vma = Swimmer(T_deb_sim, T_fin_sim)

    Définition de des allures VMA pour des temps au 400 entre 8:00 et 5:45.

    Sortie obtenue : 

    allure VMA

8min0sec ----- 0min54sec ----- 0min57sec ----- 2min0sec ----- 2min6sec
7min45sec ----- 0min52sec ----- 0min55sec ----- 1min56sec ----- 2min2sec
7min30sec ----- 0min51sec ----- 0min53sec ----- 1min52sec ----- 1min58sec
7min15sec ----- 0min49sec ----- 0min51sec ----- 1min48sec ----- 1min54sec
7min0sec ----- 0min47sec ----- 0min50sec ----- 1min45sec ----- 1min50sec
6min45sec ----- 0min46sec ----- 0min48sec ----- 1min41sec ----- 1min46sec
6min30sec ----- 0min44sec ----- 0min46sec ----- 1min37sec ----- 1min42sec
6min15sec ----- 0min42sec ----- 0min44sec ----- 1min33sec ----- 1min38sec
6min0sec ----- 0min40sec ----- 0min42sec ----- 1min30sec ----- 1min34sec
5min45sec ----- 0min39sec ----- 0min41sec ----- 1min26sec ----- 1min30sec
Done!


Temps 400m ---- temps inter VMA 110% (50m) ---- 105%(50m) ---- 100%(100m) ---- 95%(100m)
