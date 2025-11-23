# VCF by CDS Filter and Annotator
A lightweight Windows x64 GUI app that fliters a vcf file to contain only coding regions and adds coding sequence identifier information
## Citations:
When using this software Cite the following:
1. Garrison, E., Kronenberg, Z. N., Dawson, E. T., Pedersen, B. S., & Prins, P. (2022). A spectrum of free software tools for processing the VCF variant call format: Vcflib, bio-vcf, cyvcf2, hts-nim and slivar. PLOS Computational Biology, 18(5), e1009123. doi: [10.1371/journal.pcbi.1009123](https://doi.org/10.1371/journal.pcbi.1009123)
2. Li, H., & Rong, J. (2021). Bedtk: Finding interval overlap with implicit interval tree. Bioinformatics, 37(9), 1315–1316. doi: [10.1093/bioinformatics/btaa827](https://doi.org/10.1093/bioinformatics/btaa827)
3. Tsiouri, O., (2025). VCF by CDS Filter and Annotator: A lightweight Windows x64 GUI app that fliters a vcf file to contain only coding regions and adds coding sequence identifier information. GitHub [https://github.com/olgatsiouri1996/VCF-by-CDS-Filter-and-Annotator](https://github.com/olgatsiouri1996/VCF-by-CDS-Filter-and-Annotator)

## Installation
1. From the `Releases` tab download `gff2bed_features.exe` and move it to:
```sh
C:\Windows\System32
```
2. Install [bedtk](https://github.com/olgatsiouri1996/bedtk)

3. Install [Windows Subsystem for Linux](https://github.com/BioGUIwslLab/WSL-Installation)

**Note: the following installation steps will be performed on Windows Subsystem for Linux**

4.  Install linuxbrew dependences:
```sh
sudo apt install build-essential procps curl file git
```
5.  Install linuxbrew:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
6.  Add linuxbrew to PATH:
```sh
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc && source ~/.bashrc
```
7.  Make link of `vcfannotate` to `/usr/local/bin`:
```sh
sudo ln -s /home/linuxbrew/.linuxbrew/bin/vcfannotate /usr/local/bin/vcfannotate
```
8. From the `Releases` tab download the GUI app `VCF by CDS Filter and Annotator.exe`

## Usage
1. Add a gff/gff3 file and a vcf file in a folder with no other files inside:

    - Example vcf file [here](https://www.ebi.ac.uk/ena/browser/view/ERZ009613)
    - Example gff file from NCBI Genomes(Genbank) with accession: GCA_000002655   
      
2. In the gff file replace the chromosome names with those of the vcf file:  

    | NCBI Chr  | VCF Chr |  
    | :--------:  | :-------: |  
    | CM00169.1 | I       |  
    | CM00170.1 | II      |  
    | CM00171.1 | III     |  
    | CM00172.1 | IV      |  
    | CM00173.1 | V       |  
    | CM00174.1 | VI      |  
    | CM00175.1 | VII     |  
    | CM00176.1 | VIII    |  

3. Then open `VCF by CDS Filter and Annotator.exe` and click `Browse`  to navigate to the folder you put the gff/gff3 file the vcf file.

4. Click `Filter vcf` to run the app.    

5. You will be notified when the program is Finished.

6. Example output can be seen [here](data/C023MABXX_5_2_AF293.cds.vcf)