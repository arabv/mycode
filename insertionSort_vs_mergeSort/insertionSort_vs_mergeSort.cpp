#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//sortowanie przez wstawianie
void insertionsort(int* tab, size_t size){
  int x,j;
  for(int i=1; i<size; i++){
    x=tab[i];
    j=i-1;
    while(j>=0 && tab[j]>x){
      tab[j+1]=tab[j];
      j--;
    }
    tab[j+1]=x;
  }
}

//funkcja laczaca
void merge(int* tab, int a, int b, int c){
    int i,j,k;
    int n1=b-a+1;
    int n2=c-b;
    int L[n1],P[n2];

    for(i=0;i<n1;i++)  {
        L[i]=tab[a+i];
    }
    for (j=0;j<n2;j++){
        P[j]=tab[b+1+j];
    }
    i,j = 0;
    k = a;
    while(i<n1 and j<n2){
        if(L[i]<=P[j]){
            tab[k]=L[i];
            i++;
        }
        else{
            tab[k]=P[j];
            j++;
        }
        k++;
    }

    while(i<n1){
        tab[k]=L[i];
        i++;
        k++;
    }

    while(j<n2){
        tab[k]=P[j];
        j++;
        k++;
    }
}

//sortowanie przez scalanie
void mergesort(int* tab, int a, int b){
  int c;
  if(a<b){
    c=(a+b)/2;
    mergesort(tab, a, c);
    mergesort(tab, c+1,b);
    merge(tab, a, c, b);
  }
}




//wyswietl tablice
void dis_array(int* tab, size_t size){
  for(int i=0; i<size; ++i){
    cout<<tab[i]<<" ";
  }
}


int main(){
  srand(time(NULL));
  int n;
  cout<<"wprowadz dlugosc tablicy"<<endl;
  cin>>n;
  double arr_ins[100];
  double arr_merge[100];
  for(int j=0; j<100; ++j){
    int tab[n],tab1[n];
    //cout<<"twoja tablica: ";
    for(int i=0; i<n; ++i){
      tab[i]=rand()%1000;
      tab1[i]=tab[i];
      //cout<<tab[i]<<" ";
    }
    cout<<"\n\n";
    size_t size;
    size=sizeof(tab)/sizeof(tab[0]);

    //insertionsort algorithm time
    clock_t start;
    clock_t begin = clock();
    insertionsort(tab,size);
    clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    cout<<"czas wykonania insertionsort "<<j+1<<" :"<<elapsed_secs<<endl;
    arr_ins[j]=elapsed_secs;

    //mergesort algorithm
    start=0;
    end=0;
    begin=clock();
    mergesort(tab1,0,n-1);
    end=clock();
    elapsed_secs=double(end-begin)/CLOCKS_PER_SEC;
    cout<<"czas wykonania mergesort "<<j+1<<" : "<<elapsed_secs<<endl;
    arr_merge[j]=elapsed_secs;

    //display_array
    //cout<<"twoja posortowana tablica: ";
    //dis_array(tab,n);
    //cout<<"\n\n"<<endl;
    //dis_array(tab1,n);
}



double max_ins=0,min_ins=arr_ins[0],avg_ins,max_mer=0,min_mer=arr_merge[0],avg_mer;
for(int i=0; i<100; ++i){
  if(arr_ins[i]>max_ins){
    max_ins=arr_ins[i];
  }
  if(arr_ins[i]<min_ins){
    min_ins=arr_ins[i];
  }
  if(arr_merge[i]>max_mer){
    max_mer=arr_merge[i];
  }
  if(arr_merge[i]<min_mer){
    min_mer=arr_merge[i];
  }
  double temp_ins,temp_mer;
  temp_ins+=arr_ins[i];
  temp_mer+=arr_merge[i];
  avg_ins=temp_ins/100;
  avg_mer=temp_mer/100;
}

cout<<"\n\n\n";
cout<<"max time: \n";
cout<<"ins: "<<max_ins<<endl;
cout<<"mer: "<<max_mer<<endl;
cout<<"min time: \n";
cout<<"ins: "<<min_ins<<endl;
cout<<"mer: "<<min_mer<<endl;
cout<<"avg time: \n";
cout<<"ins: "<<avg_ins<<endl;
cout<<"mer: "<<avg_mer<<endl;


  return 0;
}
