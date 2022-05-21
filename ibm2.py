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
q={}
for i in range(epochs):
    c_e_f_up=defaultdict(int)
    c_e_up=defaultdict(int)
    c_j_i_up=defaultdict(int)
    c_i_up=defaultdict(int)
    for i in range(len(eng_l)):
        en_toks=["*"]+eng_l[i].rstrip().split()
        es_toks=spa_l[i].rstrip().split()
        l=len(es_toks)
        m=len(en_toks)
        for i1 in range(len(es_toks)):
            deno=0
            for j1 in range(len(en_toks)):
                en=en_toks[j1]
                es=es_toks[i1]
                if((j1,i1,l,m) in q):
                    deno=deno+t[(es, en)] * q[(j1, i1, l, m)]
                else:
                    deno=deno+t[(es, en)]*1.0/(l+1)
            for j in range(len(en_toks)):
                en_w=en_toks[j]
                es_w=es_toks[i1]
                if((j,i1,l,m) in q):
                    numo=q[(j, i1, l, m)]*t[(es_w, en_w)]
                else:
                    numo=1.0/(l+1)*t[(es_w, en_w)]
                dela=numo/deno
                c_e_f_up[(es_w,en_w)]=c_e_f_up[(es_w,en_w)]+dela
                c_e_up[en_w]=c_e_up[en_w]+dela
                c_j_i_up[(j,i1,l,m)]=c_j_i_up[(j,i1,l,m)]+dela
                c_i_up[(i1,l,m)]=c_i_up[(i1,l,m)]+dela
    for iw in c_e_f_up:
        sp=iw[0]
        en=iw[1]
        prob=c_e_f_up[iw]
        t[(sp,en)]=prob/c_e_up[en]
    for ie in c_j_i_up:
        q[(ie[0],ie[1],ie[2],ie[3])]=c_j_i_up[ie]/c_i_up[(ie[1],ie[2],ie[3])]       
english_output=open("dev.en","r")
spanish_output=open("dev.es","r")
output_translate=open("output_file_ibm2.out","w")
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
            l=len(sp)
            m=len(en)
            if((n,k,l,m) in q):
                transl_prob=transl_prob*q[(n,k,l,m)]
            else:
                transl_prob=0
            if(transl_prob>val):
                val=transl_prob
                ind=n
        wr_op=str(counter)+" "+str(ind)+" "+str(k+1)+"\n"
        output_translate.write(wr_op)
    counter=counter+1