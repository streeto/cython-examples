C FILE: EXAMPLE_F2PY.F
      SUBROUTINE hypot(X,Y,H,N)

      INTEGER N
      REAL*8 X(N)
      REAL*8 Y(N)
      REAL*8 H(N)

      DO I=1,N
         H(I) = SQRT(X(I)*X(I) + Y(I)*Y(I))
      ENDDO

      END
C END FILE EXAMPLE_F2PY.F