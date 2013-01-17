#######################################################################
#
#  This makefile creates the Fortran example programs for the
#  linear equation routines in SuperLU_DIST.
#
#  Creation date:   July 29, 2003   version 2.0
#
#######################################################################
.SUFFIXES: 
.SUFFIXES: .f90 .c .o
include ../make.inc
INCLUDEDIR = -I../SRC

#F90FLAGS	= $(FFLAGS) -qfree -qsuffix=f=f90  -qflag=w:w

F_MOD	= superlupara.o superlu_mod.o
C_WRAP	= dcreate_dist_matrix.o superlu_c2f_wrap.o

F_DEXM	= $(F_MOD) hbcode1.o f_pddrive.o
F_5x5 	= $(F_MOD) f_5x5.o sp_ienv.o 

all: f_pddrive f_5x5

f_pddrive: $(F_DEXM) $(C_WRAP) $(DSUPERLULIB)
	$(FORTRAN) $(LOADOPTS) $(F_DEXM) $(C_WRAP) $(LIBS) -o $@

f_5x5: $(F_5x5) $(C_WRAP) $(DSUPERLULIB)
	$(FORTRAN) $(LOADOPTS) $(F_5x5) $(C_WRAP) $(LIBS) -o $@

.c.o:
	$(CC) $(CFLAGS) $(CDEFS) $(BLASDEF) $(INCLUDEDIR) -c $< $(VERBOSE)

.f90.o:
	$(FORTRAN) $(F90FLAGS) -c $< $(VERBOSE)

.f.o:
	$(FORTRAN) $(FFLAGS) -c $< $(VERBOSE)

clean:	
	rm -f *.o *.mod f_pddrive f_5x5


