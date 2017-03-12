#include <python3.5/Python.h>

class integer {
    int value;
    public:
    integer()
    : integer(0)
    { }
    
    integer(int value)
    : value(value)
    { }
    
    int output() {
        return value;
    }
    
};

int main(){
    integer i = integer(1);
    printf("%d\n", i.output());
    return 0;
}
