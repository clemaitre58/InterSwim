class Time(object):
    def __init__(self, minu, sec):
        self._min = minu
        self._sec = sec
        self._sec_tot = 0
        self._gen_full_sec()

    def _gen_full_sec(self):
        self._sec_tot = self._min * 60 + self._sec


class InterVMA(object):
    def __init__(self, Ti1, Ti2, i1, i2):
        self._Ti1 = Ti1
        self._Ti2 = Ti2
        self._i1 = i1
        self._i2 = i2


class Swimmer(object):
    def __init__(self, T_start, T_end):
        self._T_start = T_start
        self._T_end = T_end
        self._step = 15
        self._l_T = []
        self._l_i_100 = []
        self._l_i_50 = []
        self._gen_scale()
        self._gen_vma()

    def _gen_scale(self):
        debut = self._T_start._sec_tot
        fin = self._T_end._sec_tot
        i = debut
        while i >= fin:
            self._l_T.append(i)
            i = i - self._step

    def _gen_vma(self):
        i110 = 110
        i105 = 105
        i100 = 100
        i95 = 95

        for i in self._l_T:
            sec110 = i / 8 / (i110 / 100)
            sec105 = i / 8 / (i105 / 100)
            sec100 = i / 4 / (i100 / 100)
            sec95 = i / 4 / (i95 / 100)
            T110 = conv_tot_sec(int(sec110))
            T105 = conv_tot_sec(int(sec105))
            T100 = conv_tot_sec(int(sec100))
            T95 = conv_tot_sec(int(sec95))

            self._l_i_50.append(InterVMA(T110, T105, i110, i105))
            self._l_i_100.append(InterVMA(T100, T95, i100, i95))


def conv_tot_sec(tot_sec):
    if tot_sec > 60:
        minute = tot_sec // 60
        sec = tot_sec % 60
    else:
        minute = 0
        sec = int(tot_sec)

    return Time(minute, sec)


def time_from_pma(time, percent):
    return time / (percent / 100)


if __name__ == '__main__':
    T_deb_sim = Time(8, 00)
    T_fin_sim = Time(5, 45)

    allure_vma = Swimmer(T_deb_sim, T_fin_sim)

    print('allure VMA')

    for i in range(len(allure_vma._l_T)):
        T_sim = conv_tot_sec(allure_vma._l_T[i])
        chaine = str(T_sim._min) + 'min' + str(T_sim._sec) + 'sec'
        chaine += ' ----- ' + str(allure_vma._l_i_50[i]._Ti1._min) + 'min'
        chaine += str(allure_vma._l_i_50[i]._Ti1._sec) + 'sec'
        chaine += ' ----- ' + str(allure_vma._l_i_50[i]._Ti2._min) + 'min'
        chaine += str(allure_vma._l_i_50[i]._Ti2._sec) + 'sec'
        chaine += ' ----- ' + str(allure_vma._l_i_100[i]._Ti1._min) + 'min'
        chaine += str(allure_vma._l_i_100[i]._Ti1._sec) + 'sec'
        chaine += ' ----- ' + str(allure_vma._l_i_100[i]._Ti2._min) + 'min'
        chaine += str(allure_vma._l_i_100[i]._Ti2._sec) + 'sec'
        print(chaine)

    print('Done!')
