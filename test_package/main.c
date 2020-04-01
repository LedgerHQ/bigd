#include <bigd.h>

int main() {
    BIGD value = bdNew();
    
    bdFree(&value);

    return 0;
}
