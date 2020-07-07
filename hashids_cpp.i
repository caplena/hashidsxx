%module hashids_cpp

%{
#include "hashids.h"
#include <list>
#include <vector> 
%}

%include "std_string.i"
%include std_vector.i 

namespace std {
  %template(IntVector) vector<int>; 
}

%include "hashids.h"
