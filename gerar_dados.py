import os, random
from datetime import datetime, timedelta
import numpy as np, pandas as pd

random.seed(42); np.random.seed(42)
RAW = "data/raw"
os.makedirs(RAW, exist_ok=True)
DI, DF = datetime(2025,1,1), datetime(2025,6,30)
N = 5000

produtos_base = [
    ("Dove","Cuidados Pessoais","Sabonete 90g",4.50),
    ("Dove","Cuidados Pessoais","Shampoo 400ml",21.90),
    ("Dove","Cuidados Pessoais","Condicionador 400ml",22.90),
    ("Dove","Cuidados Pessoais","Desodorante 150ml",18.50),
    ("Rexona","Cuidados Pessoais","Desodorante 150ml",16.90),
    ("Rexona","Cuidados Pessoais","Antitranspirante 50ml",14.50),
    ("Vasenol","Cuidados Pessoais","Hidratante 200ml",19.90),
    ("Vasenol","Cuidados Pessoais","Hidratante 400ml",29.90),
    ("Lux","Cuidados Pessoais","Sabonete 85g",3.90),
    ("Seda","Cuidados Pessoais","Shampoo 325ml",15.90),
    ("Seda","Cuidados Pessoais","Condicionador 325ml",16.90),
    ("Clear","Cuidados Pessoais","Shampoo 400ml",23.90),
    ("OMO","Limpeza","Sabão em Pó 800g",18.90),
    ("OMO","Limpeza","Sabão Líquido 3L",39.90),
    ("Comfort","Limpeza","Amaciante 1L",12.90),
    ("Cif","Limpeza","Multiuso 500ml",9.90),
    ("Brilhante","Limpeza","Sabão em Pó 1kg",17.50),
    ("Knorr","Alimentos","Caldo Galinha 57g",2.90),
    ("Knorr","Alimentos","Sopa Instantânea 63g",4.50),
    ("Hellmanns","Alimentos","Maionese 500g",12.90),
    ("Hellmanns","Alimentos","Ketchup 380g",8.90),
    ("Kibon","Alimentos","Sorvete 1.5L",24.90),
    ("Ades","Alimentos","Bebida de Soja 1L",9.90),
    ("Maizena","Alimentos","Amido de Milho 500g",7.50),
    ("Fofo","Cuidados Pessoais","Sabonete 90g",3.50),
]
prod = []
for i,(m,c,f,p) in enumerate(produtos_base,1):
    prod.append({"sku":f"SKU{i:04d}","descricao_produto":f"{m} {f}","marca":m,
                 "categoria":c,"formato":f,"preco_unitario":p})
dfp = pd.DataFrame(prod); dfp.to_csv(f"{RAW}/produtos.csv",index=False)

canais=["Grande Varejo","Atacado","Farmácia","E-commerce","Distribuidor"]
regioes=["Sudeste","Sul","Nordeste","Centro-Oeste","Norte"]
skus=dfp["sku"].tolist()
w=np.random.dirichlet(np.ones(len(skus))*0.8); w=w/w.sum()
dias=(DF-DI).days
# fator sazonal por mês (jun mais alto pra criar tendência)
saz={1:1.0,2:0.92,3:1.05,4:0.98,5:1.10,6:1.15}
ped=[]
for i in range(1,N+1):
    d=DI+timedelta(days=int(np.random.randint(0,dias+1)))
    mfac=saz[d.month]
    if np.random.rand()<(mfac-0.9):  # leve viés de volume por mês
        d=DI+timedelta(days=int(np.random.randint(0,dias+1)))
    sku=np.random.choice(skus,p=w)
    q=int(np.random.choice([6,12,24,48,96],p=[.3,.35,.2,.1,.05]))
    ped.append({"id_pedido":f"PED{i:06d}","data_pedido":d.strftime("%Y-%m-%d"),
        "sku":sku,"quantidade":q,"canal_venda":random.choice(canais),
        "regiao":random.choices(regioes,weights=[.45,.20,.18,.10,.07])[0],
        "id_cliente":f"CLI{np.random.randint(1,500):04d}"})
dfpe=pd.DataFrame(ped); dfpe.to_csv(f"{RAW}/pedidos.csv",index=False)

est=[]; da=DI
while da<=DF:
    for sku in skus:
        pr=np.random.randint(200,800)
        qd=np.random.randint(0,pr) if np.random.rand()<0.20 else np.random.randint(pr,pr*3)
        est.append({"data_referencia":da.strftime("%Y-%m-%d"),"sku":sku,
            "quantidade_disponivel":qd,"ponto_reposicao":pr,
            "centro_distribuicao":random.choice(["CD-SP","CD-RJ","CD-PE","CD-RS"])})
    da+=timedelta(days=7)
dfe=pd.DataFrame(est); dfe.to_csv(f"{RAW}/estoque.csv",index=False)

ent=[]
for _,r in dfpe.iterrows():
    dp=datetime.strptime(r["data_pedido"],"%Y-%m-%d")
    pp=int(np.random.choice([3,5,7,10])); dprom=dp+timedelta(days=pp)
    rd=np.random.rand()
    if rd<0.80:
        de=dp+timedelta(days=int(np.random.randint(1,pp+1))); st="Entregue"
    elif rd<0.95:
        de=dprom+timedelta(days=int(np.random.randint(1,8))); st="Entregue com Atraso"
    else:
        de=None; st="Pendente"
    ent.append({"id_pedido":r["id_pedido"],"data_prometida":dprom.strftime("%Y-%m-%d"),
        "data_entregue":de.strftime("%Y-%m-%d") if de else None,"status_entrega":st,
        "transportadora":random.choice(["LogFast","TransBrasil","EntregaJá","RápidoSul"])})
dfen=pd.DataFrame(ent); dfen.to_csv(f"{RAW}/entregas.csv",index=False)
print("Dados gerados:",len(dfp),len(dfpe),len(dfe),len(dfen))
