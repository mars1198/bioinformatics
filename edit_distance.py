
from numpy import zeros
def edDistDP(x,y):
    # Create distance matrix
    D = zeros((len(x) + 1, len(y) + 1), dtype = int)
    
    # Initialize the first column of matrix
    D[1:,0] = range(1, len(x) + 1)
    
    # Initialize the first row of matrix
    D[0, 1:] = range(1, len(y) + 1)
    
    # Fill in the rest of matrix
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            distHor = D[i, j-1] + 1
            distVer = D[i-1, j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1, j-1]
            else:
                distDiag = D[i-1, j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    return D[-1][-1]
x = 'HETPKSDMEMERFKNFPPCLVCEIANDQKTVFHCSMDWYIFSNTPTDNNYAELIWYHAAAPTNYINEHCSRWYMVAPNHLELHNNAYNLYYQALHKFAYMFDTYREATPDCDRALPISCNCSQCVVLSEFWYQGFCHMLGYPEFPWVKIDMHMRFERCCHGLQQMPHTVMVLGDKGFVNGLDKDKCYRTWDFHVDACTTDIQDSSRCNIEILEPNKAYSCYIIFPCLTMHQCQLYKAMKFLGEVAGSRTPHMTWQRIYDARGRNTMFPAIRCGSKWIEGPETQAWWCLSYPKTGHANDCVLLATECLLLLGGMQPLPTKREHWRHQEYWNWWTLFQIEQHIEHDQRRKMKRNNDQKHKNSMNMHCIMVFTLTGTCFWWVPGQLQLEDDRIDYRLPLQPGNCHKKIGQTREMLWHVDIYMRRMCLLGEPLTMSRLCKVWRTSDARNILNVYRAREQQDDMNFHDYMQLACLLDHMIYSCTDVIDQCRCQKGKYRLFCTILEMSQWLGGVERQWKKPNCKELRWISQWTQHCYGLPGKTPPHQNQSLMGNKRLMPGNMSHHDPPAAHAIPAMQLRDYVGDIWPQSGQGEFLYDIIWSYTSVVDTEWPVMGTDYNHVVNQCDENSNPFQDFYIVCYTGGAWARKATKNRLEFRCFNNLVKMLWDAPNKFQADIIMFWEQCNNWCHQAPWAHIKYMMINTPPMPFFWFMVMRCNWCWIHEAIRA'
y = 'HETIVSLFPLWDSDMEMERFSHFPPEEYDRHMHTPTDNNYAEMIQYHFCEAQIRWAAPTTYAPYIIENLMYCGMVCWYMVARTNLYYRALHKWTYARATVWQKEDCDRALPVVWSEFWYFGFCHMLGYPEFPHTELNVPMFEEACSHGLQQMPHTVMVLQVKGFVNGLNKPEGGEVHVDACTTDIQDSSIPSSWNRYIMIEILEPNKAYSCYIIFPCLKEDKAMKFLGEVAGSRWPHMYWAPGRNTMFPCCIWGYENAWWCLSYPRTGHANDCVLLLLGGMQPLPTKRHHWRHQEYWNFWTLFQIEQKIEHDQRRKMKRNNDQKHIVCFKRNSMCCWQLYDQCHCHSPFQMVFTFTGTCFWWCHGCGSTFCESFNGQTQLEDDRQPLQQRKIGQTRDMLWHVDARDKLYMRRMYLLGEPLTMYGIKRLCKVWRTSDARNILNCYRAREQQDDMNFHDYMQLACLLDHVINQSGQGVIDQTFRCQKRKYRLFCTILEELSQWIYLKLGVERQWKSSACARPYTQHCYGLVGKTPPGQPGDTMIDYSCVSVTNSRAGMPMCDHAIPANHLRDAVGINMIWFLYDIITSYTSVVDTEWPVMETDWWMNWYNHKVNQGDEYSNPFQDAKQKRKYKVCYTGGKWDECLAKFNMLWDAPNKFQADIIMFWEMCNNWCHQAPWAHIKTMEINPPPMPFFWFMVMRFQMMKEPEWNWCWIHWAIRA'

print (edDistDP(x, y))
