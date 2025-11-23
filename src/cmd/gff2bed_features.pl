use strict;

########################################################################
# gff2bed_features.pl by HalfonLab 
#
#my own gff2bed#
#June 19 2012, modified July 20 2012#
#modified 06-23-2015 to make generic
#modified 11-10-2022 to take selected features only
#note that there is limited error-checking built in, use with caution
#November 15 2025 modified by Olga Tsiouri <olgatsiouri@outlook.com>
#fixed id issue so that it can handle any letter and '=' and added all 9 gff3 columns to the output
########################################################################

#USAGE:file name on cmd line, feature name on command line 
die "USAGE: ./gff2bed_features.pl <gff_file_name> <feature_type>" unless @ARGV==2;

my $filename = shift;
my $feature = shift;

open(INFILE, "<$filename") or die "bad file name: $!";

while(<INFILE>){
	chomp;
	last if $_ =~ /##FASTA/;
	next if $_ =~ /^#/;
	next unless $_ =~ /\w/;
	my @F= ();
	@F=	split(/\t/);
	next unless $F[2] eq "$feature";
	
	my $attrs = $F[8];

	my $a = ".";   #default value if no match
	if ($attrs =~ /([^=;]+)=([^;]+)/) {
		my $value = $2;
		$value =~ s/.*://;   #remove prefix before colon
		$a = $value;
	}
	
	my $astart = $F[3]-1;  #correct for zero-based coordinates going from gff to bed
	my $aend = $F[4];

	my $ascore = $F[5];	
	my $astrand = $F[6];
	my $asource = $F[1];
	my $atype = $F[2];
	my $aphase = $F[7];

	print  "$F[0]\t$astart\t$aend\t$a\t$ascore\t$astrand\t$asource\t$atype\t$aphase\t$attrs\n" ;
	
} #end while	

close(INFILE);

__END__	
	

	
	

