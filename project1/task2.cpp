#include <openssl/bn.h>
#include <openssl/err.h>
#include <string>
#include <iostream>
#include <cstring>

using namespace std;

int main(){
    BIGNUM* hex_p = BN_new();
    BIGNUM* hex_q = BN_new();
    BIGNUM* hex_e = BN_new();
    BIGNUM* hex_d = BN_new();

    BN_hex2bn(&hex_p,"F7E75FDC469067FFDC4E847C51F452DF");
    BN_hex2bn(&hex_q,"E85CED54AF57E53E092113E62F436F4F");
    BN_hex2bn(&hex_e,"0D88C3");
    /*
    what i've learned
    You can decrypt the original message using public key or private key.
    This can be done by fermat's littel theorem

    let p and q be prime numbers.
    and let e be relatively prime number of Totient number of n (p*q)

    C = m^e mod n (m<n)
    M = C^d mod n

    m^de mod n is M 

    x^p mod p = x
    x^(p-1) mod p =1 where p is a prime number

    Since e is relatively prime to n so it can be rewritten as k(p-1)(q-1) +1
    by applying fermat's little theorem, 
    m^de mod n -> m^(p-1)(q-1) * m mod n
    therfore, 
    1 * m mod n = m 
    */

   /*
   task 1
   Find out d with known p,q,e
   */

   /*
   g++ -I/opt/homebrew/opt/openssl@3/include -L/opt/homebrew/opt/openssl@3/lib -lssl -lcrypto task2.cpp -o task2
   */
    BIGNUM *n = BN_new();
    BIGNUM *phi = BN_new();
    BIGNUM* one = BN_new();
    BN_one(one);
    
    BN_CTX *ctx = BN_CTX_new();
    BN_CTX *ctx1 = BN_CTX_new();
    BN_mul(n,hex_p,hex_q,ctx);
    BN_sub(hex_p,hex_p,one);
    BN_sub(hex_q,hex_q,one);
    BN_mul(phi,hex_p,hex_q,ctx1);

    if (BN_mod_inverse(hex_d, hex_e, phi, BN_CTX_new()) == NULL){
        printf("Error: %s\n", ERR_error_string(ERR_get_error(), NULL));
        return 1;
    }
    
    char* private_key = BN_bn2hex(hex_d);
    char* phi_ = BN_bn2hex(phi);
    cout<< "private key: "<< string(private_key)<<endl;
    cout<< "phi: "<<string(phi_)<<endl;
    BN_free(hex_q);
    BN_free(hex_e);
    BN_free(hex_d);
    BN_free(phi);
    BN_free(n);
    return 0;
}