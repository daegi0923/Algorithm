#include <iostream>
#include <vector>
#include <deque>
using namespace std;



int N, K, cnt;
int s;
int e;
vector<int> belt;
deque<int> robots;
bool stop = false;
int result = 1;
void input(){
    cin >> N >> K;
    s = 0;
    e = N -1;
    belt.resize(2*N);
    robots.resize(2*N);
    for(int i = 0; i < 2*N ;i++){
        cin >> belt[i];
    }
}
void rotate(){
    s = s - 1;
    e = e - 1;
    if(s < 0){
        s = 2 * N -1;
    }
    if(e < 0) {
        e = 2 * N -1;
    }
    if(robots[e])
        robots[e] = 0;
}

void move_robot() {
    int curr = e;
    for(int i = 0; i < N-1 ; i++) {
        int next = curr;
        if(curr == 0)
            curr = 2*N -1;
        else
            curr = curr - 1;
        if(!robots[next]&&robots[curr]&&belt[next]) {
            belt[next] = belt[next] - 1;
            if(belt[next] == 0) {
                cnt = cnt + 1;
                if(cnt >= K) {
                    stop = true;
                }
            }
            robots[next] = 1;
            robots[curr] = 0;
        }
        robots[e] = 0;
    }
}

void add_robot(){
    if(belt[s]) {
        robots[s] = 1;
        belt[s] = belt[s] - 1;
        if(belt[s] == 0) {
            cnt = cnt + 1;
            if(cnt >= K) {
                stop = true;
            }
        }
    }
}

int main() {
    input();
    while(!stop) {
        rotate();
        if(result>1)
            move_robot();
        add_robot();
        if(stop) {
            break;
        }
        result = result + 1;
    }
    cout << result;
    return 0;
}