#######################################################################
#
#  This makefile creates the example programs for the linear equation
#  routines in SuperLU_DIST.
#
#  The command
#       make
#  without any arguments creates all the example programs.
#  The command
# 	make double
#  creates double precision real example programs.
#  The command
#       make complex16
#  creates double precision complex example programs.
#
#  The executable files are called
#       double real:	pddrive pddrive_ABglobal pddrive1
#                       pddrive1_ABglobal pddrive2 pddrive3 pddrive4
#	double complex: pzdrive pzdrive_ABglobal pzdrive1
#                       pzdrive1_ABglobal pzdrive2 pzdrive3 pzdrive4 
#
#  Alternatively, you can create example programs individually by
#  typing the command (for example)
#	make pddrive
#
#  To remove the object files after the executable files have been
#  created, enter
#       make clean
#
#######################################################################
include ../make.inc
INCLUDEDIR = -I../SRC

TAUOPT=-optVerbose -optTauSelectFile=$(HOME)/projects/SuperLU_benchmarking/SuperLU_DIST_2.5/SRC/select.tau -optKeepFiles
THISLOADER = tau_cc.sh $(TAUOPT) -tau_makefile=$(TAULIBDIR)/Makefile.tau-mpi-pdt-pgi

DEXM	= pddrive.o dcreate_matrix.o sp_ienv.o dreadtriple.o dreadhb.o 
# pdgstrs_lsum_X1.o pdgstrf_X1.o
DEXM1	= pddrive1.o dcreate_matrix.o dreadtriple.o dreadhb.o
DEXM2	= pddrive2.o dcreate_matrix.o dreadtriple.o dreadhb.o
DEXM3	= pddrive3.o dcreate_matrix.o dreadtriple.o dreadhb.o
DEXM4	= pddrive4.o dcreate_matrix.o dreadtriple.o dreadhb.o
DEXMG	= pddrive_ABglobal.o dreadtriple.o dreadhb.o
DEXMG1	= pddrive1_ABglobal.o dreadtriple.o dreadhb.o sp_ienv.o 
DEXMG2	= pddrive2_ABglobal.o dreadtriple.o dreadhb.o
DEXMG3	= pddrive3_ABglobal.o dreadtriple.o dreadhb.o
DEXMG4	= pddrive4_ABglobal.o dreadtriple.o dreadhb.o
ZEXM	= pzdrive.o zcreate_matrix.o zreadhb.o zreadtriple.o #pzgstrf_X1.o
ZEXM1	= pzdrive1.o zcreate_matrix.o zreadhb.o
ZEXM2	= pzdrive2.o zcreate_matrix.o zreadhb.o
ZEXM3	= pzdrive3.o zcreate_matrix.o zreadhb.o
ZEXM4	= pzdrive4.o zcreate_matrix.o zreadhb.o
ZEXMG	= pzdrive_ABglobal.o zreadhb.o
ZEXMG1	= pzdrive1_ABglobal.o zreadhb.o
ZEXMG2	= pzdrive2_ABglobal.o zreadhb.o
ZEXMG3	= pzdrive3_ABglobal.o zreadhb.o
ZEXMG4	= pzdrive4_ABglobal.o zreadhb.o

all: double complex16

double:    pddrive pddrive1 pddrive2 pddrive3 pddrive4 \
	   pddrive_ABglobal pddrive1_ABglobal pddrive2_ABglobal \
	   pddrive3_ABglobal pddrive4_ABglobal

complex16: pzdrive pzdrive1 pzdrive2 pzdrive3 pzdrive4 \
	   pzdrive_ABglobal pzdrive1_ABglobal pzdrive2_ABglobal \
	   pzdrive3_ABglobal pzdrive4_ABglobal

pddrive: $(DEXM) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXM) $(LIBS) -lm -o $@

pddrive1: $(DEXM1) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXM1) $(LIBS) -lm -o $@

pddrive2: $(DEXM2) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXM2) $(LIBS) -lm -o $@

pddrive3: $(DEXM3) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXM3) $(LIBS) -lm -o $@

pddrive4: $(DEXM4) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXM4) $(LIBS) -lm -o $@

pddrive_ABglobal: $(DEXMG) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXMG) $(LIBS) -lm -o $@

pddrive1_ABglobal: $(DEXMG1) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXMG1) $(LIBS) -lm -o $@

pddrive2_ABglobal: $(DEXMG2) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXMG2) $(LIBS) -lm -o $@

pddrive3_ABglobal: $(DEXMG3) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXMG3) $(LIBS) -lm -o $@

pddrive4_ABglobal: $(DEXMG4) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(DEXMG4) $(LIBS) -lm -o $@

pzdrive: $(ZEXM) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXM) $(LIBS) -lm -o $@

pzdrive1: $(ZEXM1) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXM1) $(LIBS) -lm -o $@

pzdrive2: $(ZEXM2) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXM2) $(LIBS) -lm -o $@

pzdrive3: $(ZEXM3) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXM3) $(LIBS) -lm -o $@

pzdrive4: $(ZEXM4) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXM4) $(LIBS) -lm -o $@

pzdrive_ABglobal: $(ZEXMG) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXMG) $(LIBS) -lm -o $@

pzdrive1_ABglobal: $(ZEXMG1) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXMG1) $(LIBS) -lm -o $@

pzdrive2_ABglobal: $(ZEXMG2) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXMG2) $(LIBS) -lm -o $@

pzdrive3_ABglobal: $(ZEXMG3) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXMG3) $(LIBS) -lm -o $@

pzdrive4_ABglobal: $(ZEXMG4) $(DSUPERLULIB)
	$(THISLOADER) $(LOADOPTS) $(ZEXMG4) $(LIBS) -lm -o $@

.c.o:
	tau_cc.sh $(TAUOPT) -tau_makefile=$(TAULIBDIR)/Makefile.tau-mpi-pdt-pgi $(CFLAGS) $(CDEFS) $(BLASDEF) $(INCLUDEDIR) -c $< $(VERBOSE)

.f.o:
	$(FORTRAN) $(FFLAGS) -c $< $(VERBOSE)

clean:	
	rm -f *.o p[dz]drive p[dz]drive[1-9] \
	p[dz]drive_ABglobal p[dz]drive[1-9]_ABglobal


