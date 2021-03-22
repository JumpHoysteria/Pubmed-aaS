from getIDList import getUIDList
import time
from tqdm import tqdm

## Produce Validation Set
# Creates File with PMID's of Validated Papers

query = '''Gata3 targets Runx1 in the embryonic haematopoietic stem cell niche.
Protocol for the Generation of Definitive Hematopoietic Progenitors from Human Pluripotent Stem Cells[Title] AND Elefanty[Author]
Single-cell transcriptomics identifies CD44 as a marker and regulator of endothelial to haematopoietic transition[Title]
Biomimetic aorta-gonad-Mesonephros-on-a-Chip to study human developmental hematopoiesis.[Title] AND Sugimura[Author]
Combination of SB431542, Chir9901, and Bpv as a novel supplement in the culture of umbilical cord blood hematopoietic stem cells[Title] AND Zarrabi[Author]
Distinct Waves from the Hemogenic Endothelium Give Rise to Layered Lymphoid Tissue Inducer Cell Ontogeny[Title] AND Simic[Author]
Overexpression of p21 Has Inhibitory Effect on Human Hematopoiesis by Blocking Generation of CD43+ Cells via Cell-Cycle Regulation[Title] AND Zeng[Author]
Embryonic lineage tracing with Procr-CreER marks balanced hematopoietic stem cell fate during entire mouse lifespan[Title] AND Zheng[Author]
Hemogenic Endothelial Cells Can Transition to Hematopoietic Stem Cells through a B-1 Lymphocyte-Biased State during Maturation in the Mouse Embryo.[Title] AND Kobayashi[Author]
Effects of mouse fetal liver cell culture density on hematopoietic cell expansion in three-dimensional cocultures with stromal cells[Title]
The versican-hyaluronan complex provides an essential extracellular matrix niche for Flk1+ hematoendothelial progenitors[Title]
Niche derived netrin-1 regulates hematopoietic stem cell dormancy via its receptor neogenin-1[Title] AND Trumpp[Author]
RUNX1-205, a novel splice variant of the human RUNX1 gene, has blockage effect on mesoderm-hemogenesis transition and promotion effect during the late stage of hematopoiesis[Title] AND Sun[Author]
Overexpression of HOXA9 upregulates NF-kappaB signaling to promote human hematopoiesis and alter the hematopoietic differentiation potentials[Title] AND Zeng[Author]
ZNF143 mediates CTCF-bound promoter–enhancer loops required for murine hematopoietic stem and progenitor cell function[Title]
Generation of reconstituted hemato-lymphoid murine embryos by placental transplantation into embryos lacking HSCs[Title]
A splicing factor switch controls hematopoietic lineage specification of pluripotent stem cells[Title]
Hepatic stellate and endothelial cells maintain hematopoietic stem cells in the developing liver[Title]
"Yolk sac, but not hematopoietic stem cell–derived progenitors, sustain erythropoiesis throughout murine embryonic life"
Wip1 regulates hematopoietic stem cell development in the mouse embryo[Title]
Sox17-mediated expression of adherent molecules is required for the maintenance of undifferentiated hematopoietic cluster formation in midgestation mouse embryos[Title]
''' 


with open('ValidationPMID.txt', 'w') as f:
    for line in tqdm(query.splitlines(), smoothing=1):
        #time.sleep(0.4)
        res, con = getUIDList(line)
        #print(line)
        if len(res) > 1 or len(res) == 0:
            print("ERROR: " + line + " gives " + str(len(res)) + " results!")
        f.write(str(res[0]) + "\n")
    f.close()
