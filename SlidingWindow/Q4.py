

# Given a word pat and a text txt. Return the count of the occurences of anagrams of the word in the text.

# Input:
# txt = aabaabaa
# pat = aaba
# Output: 4
# Explanation: aaba is present 4 times
# in txt.

def answer(txt,pat):
    dic = {}
    for ele in pat:
        if ele not in dic:
          dic[ele]=0
        dic[ele]+=1
    # print(dic)
    count = len(dic)
    n = len(txt)
    k=len(pat)
    ans = 0
    i=-1
    # print(txt)
    for i in range(k-1):
        if txt[i] not in dic:
            dic[txt[i]] = +1
            count+=1
        else:
            dic[txt[i]]-=1
            if dic[txt[i]]==0:
                count-=1
    # print(dic,txt[:i+1],count,k)
    start  = 0
    # print(i)
    end = i
    # print(txt)
    while end<n-1:
        end+=1
        if txt[end] not in dic:
            dic[txt[end]]=-1
        else:
          dic[txt[end]]-=1
        
        flag = 0
        for key in dic:
          if dic[key]!=0:
            flag=1
        if flag==0:
          ans+=1
        # print(dic,txt[start:end+1],ans,txt[end])
        dic[txt[start]]+=1
        start+=1
    print(ans)
    return ans


# txt = "aabaabaa"
# pat = "aaba"


# txt = "forxxorfxdofr"
# pat = "for"

# txt = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
# pat = "kkkkk"

# txt = "eaylnlfdxf"
# pat = "irc"

# txt = "wljfrimpmyhchzriwkbarxbgfcbceyhjugixwtbvtrehb"
# pat = "b"

txt = "ujdmzqhxvamqrhvamxzuouopbusubsjzqcqfcrpmpgfcdxcrzxhfbpuhacramjqzqquzjouxmprugduqocpsfsmcvvbmxzhkzjdyvfmbfoipdmeosscqzpvhurumzarpzcvmcgjuxjdqabfpqoomqfmuubhxancnafsxzbubebvnfhlmpctfwmaubbqhpqquafzucpdupcoxzjgvvfxmqrzcoushrjmmsxhujmjpfvsgqopsucozardbzqmrucpbfmucuhqqzmxavcjvofacxfbsuxbqsqhpahuzgqmmrdpvjmcomuqzupuzrrpuusahcvvmhxjzufmfzacrbjqsummrxoqzgocqpdbupqdtsmozwsradrbfapoocvuugbzxczmhuufphmscujxzqvmpsmjqqqqjupfjbqhbupfqpsmamhzcavgoqomxudvszxruzmrccumbpzrhzfpajouqcgjozvrcpuvxqaduhcmmfuqbxmqsusqbqqcjupouvomhqudhucjpmzsragmfzzxrfsmcpbxvaulikzhvlmjpnouuropmsuqoxhfmjcqprfucmxuzavjzsqpbbqzaugumvhcdjoazruqqmufbsmbcapfzmczpduprxogsjmvxhvuchuqqqvrcfoujusmbzsurmhqxmdzfopqcauzubmqpjxcgphvadhzpxxkmnjlcajmxdouvoamscqxbpgmuvphqhrfzqucbsmujpczzqurfajiobhsbwktbccspqjuzvfmbvpmqmcxzhqquxzabamgroduphcfjrsouuhhsqpqmjszfcvdbugpcoauxczxbzqvuufraqujopmmmrlrnragnldauovgnxqudpjqcbpcqpzoghscrxujmomuzffxauasqhrmmvzqvubwlmhdrpgcozczmhruqaumxspfcfjqbqvuuozbasxjpvqumvhjuuhqzadbcmgcrfuqozcmbrsmoxuspjxmpufvzqapqqrjuspcppmuhqbodmszcvmjzfgqaamxubuqhzcvruxofamvudpbxhzozocqumuqjvsfpqrmfxgujphcmcrsauzbquahqpjsqzqsxczuvubzgucbfrxjoqocmvpummpmdarfhqrgrydabsbvgzosqasqurmmxqbpzuuhrofdujxucccpfjbmmzhpqavxuhaqmfmvxmmvdqpugrscqzbrjojshcqbuozpazfpuucxzvuzuqdhmbmxcjuogzbfspvcqqmfocpuasjpramuqrhkcusmgpqzbqprvuhazdmhjmsxcqfzjfcapuxorvqobmuuwwfkeumrxouslhxwjpvmsrozdvcbjgufpaumuxfrhhzmcmxpbcsazoqjqqquutzrwotonqzzoavsvrdfhsaczqpmghpjqujbmruxqpmcfoumbcuxusjvqoaufbcumcmhmjbzxrphzqrpuqxasufqpugdoczmvuzxhhsrjizszbaczjvcoxmdzjvhfcsmaqhxpfmsuqruuumbqoqgurppbfzdxjvvcpufmsmaacqzguoppouxqjbrhmrusqquczmhzgoubzmpjpuszvovdmcauhuqpxmfxqucrbqazghsfjqrmcnwhrszzugcqcmvdqcjzbhhqmfaupsxvoamfuxmuqpburjprocuzkmqazrqvrbmmospufacgzuuxcupjhqsqbxzphcjufvdomqhgmrucummzhzxupoqcopjavmfdxfusurqqbcjzspvabaovxvguxpmuhzqjzqumcqrafrudpubbpjsqhfmszmoccibsvcowzauxsuomzahprjccgduzzbqjqsomqvvbprmhcqmxfpuuffvymutvmbqqhpzjqqamdrxmprszuucgzxcmuhfpavvjsuobocufmdhzmsuupzjccraqqxbfufomuzjgpxbcasopqvrmvqhuodjujzpgfcrzmqxuumpqqcxupmhubasqzfcrvbovmshakdwvsocqjdufqgmqqhxpbrhupoufmuaxcrzmbzpavumzcjspsalpikolqzcggddlxmiuivnqhfzozgjuvfcmpcpxqsqhcxuhabpqmujrobzaqurmsmduvkzgenayzbwfesfsgfozpeynzsummepjcjpzafbuhqmmxuqczoxqgpqbmuscrauprodhzmfvusvoqptsofucbxrbqcqmhhupzzpsvfuusfqvcajzromampugdmqojxbxayipirvvxcmbjspquxmqcosuzzapucqrbmgouqhjmuhffavdrzprqsjbmvhacuuqhmxoqbcpjpfpurzgzuzvxsaocmmfudqrxbkzbixjubvsmsjvqxcqzhudurazmmpuqpzgjhqxmucopouraffbchmxfvgzzmuuuocabmauqqmphpjfdsqqjozcrrusvcbxpekbjzvvtkbihwrbdelhlisorpjgpxudmcuhcoojhpvafxmqvsmuamcsfrzzuzqqbuqbxpefwtihobmvmqncebqteznmmyccukhdoirtdmnvrdzrmaxpjqubhcbguurmumoxqjvcuvspfqoqzshfzcapmaxquzcjucomrfxvuuzzbpbqvhmjraugpsfpmhqoqdmcsmpozmmejthbuucsxqbpzrpmuqugodrfjhzcqhzxvpavsaubfummjmcoqjarxrvzqompqmjcpxfmcpvgusafsmquuohbubhqcuzzdmpuzaqqhcsavrgfzzjxbmrchupxdsfvumbmquoupjcqohhzxbsjdpqqourmqqvccpujaufmrmovmupczfgbasxuzuzzsbmruqaqpxumozpmarccvmhbqphufxojujgvfdqcshpkclrfgvaxpfchqpzxqofmbohszagmbuzvupscmmuqdjrjruucqbquqzqchfsuxuocpmzpjsrgmvxuavzqahdubjmpfcomrdqcumpgoauxbzmjrumspbsjarmfvuqvxupozqhfchzqcbxvcklxxmpxfqawkrrtqqkoucszphqmgdxmujobvmuzsbfpmchqpfjuxaaqrucqzvrtfmiruyfixucmzfcpdvhqambrjqvuguomuphscqqxoaupszmxfrbjzufzpjsquvocazhsbgorjcfrxmbaphupqmqudmumqvzxcoaqdjuzaoxqupbcxmqmvpujhqrczsgfuhzrbucmspvmfposjuzcdmquuumvpxfbcmzogqmaaujvfcqzsbxrphrhqsxvuujuudrqhfbpcvpozzsfrmzmouaqpahxgjqcqbmcmmqfgjquxpaofhmajbbzoucrzxsvmqpsprcquhuvzmduccfuqzzumcosoqpfdujqamjvbgruhpcsxmbmrhuqzxvpasbmbvhvozmqzjuqxcdphumucrqraqcfxmupozsfagpujbkquujtyzaqhxsrmmrczuxjazbmdvuofqqzmoupvaupbccughqjspftdnpsauiuzjbqhjrxquouacumcbsovahzrpdmppqsfgumfzmvcqxkibgehsrybspcxuuzsvfazomudqqcargoxhmqrjzupjfbmbqpumhcvdvgvsuxpphzxcuobumdmrohcrfqmufqpqbzamqcujajszbwuacpiqjburmqoxgqzmppruhocbcuzfvpqvudhsxaqmzscmafujqzftaqxvmpcrzuosqjcouzbhcupzjqhvuuqsrfpmxmdmbfgaseususaqfvfmmzgzpduouqrchazphjxbjrcumxqqbcpovmfvhsmbrmdjuuzqaccxupavmfgxzpmqsoqchupqzojurbwuwlassjxqmzouujmrsbzgjqhfbazcuvuscdupvommprqhpqafxcxrombmzpcupvgqofchzxuqapmhqsqufdzuusmjjvabcrcjuyqzuqbdmxvrbammschxmuofjrzavpchcpuopzqsfgjuqubyzdfqoxhqcuqjmacrufsaqhobuzpxsdmzvpzmbrmgcpvuujnviomrruagjuvpmcjpcfvqxafmrhxsmoquushzzupqczobbdqmoirpyaoxbcofmqrvzhzppjcmxfjguvaqqbosmqudruhuzcmuaspqojhsouzasmagxfcrmmzbpdxuqphcbfpjmurcvzvquuqaqqodhwegxaopmxpzzhmqkirocqqxbmhpsovzrzafqazjcgurbmjcuhsmpfxupomvqudukwusyqrnpgaghfstqorpfoscubopvmqujbquuqzfqarxhmcacszmzjhpgxmdvuxacgbcvosmzpdmuvfhfqbuoxrpqqpjzcrumjhmqusuazojqbummhuumgbmfxvopjarxzrqsccqzpfavuudscpzhqkllznuchafrcgvaquhvcfumqbmzpuusqzboxjrzqspmopdjmxpmcqcpuqrfojbhzpuaufvmzmzbjduraqmxhsxgouscvqubpqahbzxufcmmjovcrqzcuavzqrmpoxjphsudqmfsugvtnnywlqqjbnpchczomqvmvrzgmcaxujbduufurqsmqbqxhszfappuojcoxvbbjzjrhpmuhzsazfrqdvxfumgumcqsqpmcauoqupsuudqschpqhavoabqrzmczpbjuqoxjpmrffxvugummczobhyfcvdcxzvqbpujjgmfapocxocumvfhruqamhmzqspusqruzdbbtcobxqxqhougmzbpspmuvdcfqmupjufajcvuszarzmhrqvjshxazamvcpduvqfbphbcuuczoqqgosfrpzjruxmjumqmpxcormujmcqjqsmfodusbzguaazvhqpfhmurqcpvzxubwazhughkpoxupqpbgzxauarmmbrdzfcfvuvscqqmpjmuhzjcqohuslclexozhfqxhvouaruqcpdcqubuqzcspouapjmrvfjxmmbzmsgxjkygpaiuzqfxwxnolmrbsjqquujuupafzvmammvzqqxgsphuzdmorchcpxfcbosujqucpamovmuzomdgzpfchcfbvapqzxqxqmubhsrjurtchqgwnrrxcujauhfsopxmcmjzumoaqzqvhrmfrbuppqusgvdqzbxc"
pat ="cujauhfsopxmcmjzumoaqzqvhrmfrbuppqusgvdqzbxc"

answer(txt,pat)
# print(len(txt)-len(pat)+1)