from collections import defaultdict
dict_of_eng_words={}
english=open("corpus.en","r")
spanish=open("corpus.es","r")
epochs=5
t={}
eng_l=[]
for i in english:
    eng_l.append(i)
spa_l=[]
for j in spanish:
    spa_l.append(j)
for i in eng_l:
    fin_sent="* "+i
    sent_tok=fin_sent.rstrip().split()
    for j in range(len(sent_tok)):
        if(sent_tok[j] in dict_of_eng_words):
            dict_of_eng_words[sent_tok[j]]=dict_of_eng_words[sent_tok[j]]+1
        else:
            dict_of_eng_words[sent_tok[j]]=1
for i in range(epochs):
    c_e_f_up=defaultdict(int)
    c_e=defaultdict(int)
    for i1 in range(len(eng_l)):
        en_sent=eng_l[i1]
        sp_sent=spa_l[i1]
        en_toks=["*"]+en_sent.rstrip().split()
        es_toks=sp_sent.rstrip().split()
        for i in range(len(es_toks)):
            deno=0
            for k in range(len(en_toks)):
                en_w=en_toks[k]
                es_w=es_toks[i]
                if((es_w,en_w) in t):
                    deno=deno+t[(es_w,en_w)]
                else:
                    deno=deno+1/dict_of_eng_words[en_w]
            for j in range(len(en_toks)):
                es_w,en_w=es_toks[i], en_toks[j]
                if((es_w,en_w) in t):
                    numo=t[(es_w,en_w)]
                else:
                    numo=1/dict_of_eng_words[en_w]
                dela=numo/deno
                c_e_f_up[(es_w,en_w)]=c_e_f_up[(es_w,en_w)]+dela          
                c_e[en_w]=c_e[en_w]+dela
    for probs in c_e_f_up:
        t[(probs[0],probs[1])]=c_e_f_up[probs]/c_e[probs[1]]
english_output=open("dev.en","r")
spanish_output=open("dev.es","r")
output_translate=open("output_file_ibm1.out","w")
counter=1
eng_l_o=[]
for i in english_output:
    eng_l_o.append(i)
spa_l_o=[]
for j in spanish_output:
    spa_l_o.append(j)
for w in range(len(eng_l_o)):
    sp=spa_l_o[w].rstrip().split()
    en="* "+eng_l_o[w]
    en=en.rstrip().split()
    for k in range(len(sp)):
        ind=0
        val=0
        for n in range(len(en)):
            if((sp[k],en[n]) in t):
                transl_prob=t[(sp[k],en[n])]
            else:
                transl_prob=0
            if(transl_prob>val):
                val=transl_prob
                ind=n
        wr_op=str(counter)+" "+str(ind)+" "+str(k+1)+"\n"
        output_translate.write(wr_op)
    counter=counter+1