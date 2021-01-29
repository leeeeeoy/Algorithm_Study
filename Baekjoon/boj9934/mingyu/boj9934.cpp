/*
Baekjoon 9934. 완전 이진 트리
url: https://www.acmicpc.net/problem/9934
writer: Mingyu
Language: C++
Date: 2021.01.25
Status: , Runtime:  ms, Memory Usage:  KB
*/

#include <iostream>

using namespace std;
 
// 트리의 level, 빌딩 번호를 담을 배열
int level, num[1024];

// 트리의 최대 높이를 담을 변수. 가장 낮은 높이는 2이므로 우선 2로 설정해둔다
int End = 2;

// 빌딩의 번호를 각 level에 담기 위해 만든 배열
int tree[11][512];

// 해당 깊이의 인덱스에서 중간값(mid)를 저장해놓기 위해 만든 배열
int depth_idx[10] = {0,};
 
// 검사의 시작 지점, 검사의 끝 지점, 해당 검사하는 곳의 깊이
void building(int start,int end, int depth) {
    // 시작값이 끝값보다 커지면 num을 다 돌았다는 뜻이 된다. 그러므로 return
    if (end - start < 0) return;
    
    // 중간값 인덱스
    int mid = (start + end) / 2;

    // 해당 깊이의 각 노드들에 값을 부여
    tree[depth][depth_idx[depth]++] = num[mid];

    // mid 인덱스를 기준으로 좌측 트리에 대해 노드값을 부여하는 재귀를 수행
    building(start, mid-1, depth+1);

    // 동일한 방식으로 mid의 우측 트리에 대해 수행
    building(mid+1, end, depth+1);
}
 
int main() {
    cin >> level;

    // level만큼 트리의 높이를 올린다.
    for (int i = 1; i < level; i++)
        End *= 2;

    for (int i = 1; i < End; i++)
        cin >> num[i];

    // 빌딩 전체(시작지점 1, 끝지점 End -1)를 재귀에 넣는다. 상단 building 함수 참조
    building(1,End-1,0);
 
    // 트리에서 각 층마다 출력을 수행해야 하므로 End값을 조절하여 각 층을 탐색 후 출력
    for (int i = 0; i < level; i++) {
        End = 1;
        for (int j = 0; j < i; j++)
            End *= 2;
        for (int j = 0; j < End; j++) {
            cout << tree[i][j] << " ";
        }
        cout << '\n';
    }
    return 0;
}



/* 주석 없는 코드
#include <iostream>

using namespace std;
 
int level, num[1024];
int End = 2;
int tree[11][512];
int depth_idx[10] = {0,};
 
void building(int start,int end, int depth) {
    if (end - start < 0) return;
   
    int mid = (start + end) / 2;
    tree[depth][depth_idx[depth]++] = num[mid];
   
    building(start, mid-1, depth+1);
    building(mid+1, end, depth+1);
}
 
int main() {
    cin >> level;

    for (int i = 1; i < level; i++) End *= 2;

    for (int i = 1; i < End; i++) cin >> num[i];

    building(1,End-1,0);
 
    for (int i = 0; i < level; i++) {
        End = 1;
        for (int j = 0; j < i; j++)
            End *= 2;
        for (int j = 0; j < End; j++) {
            cout << tree[i][j] << " ";
        }
        cout << '\n';
    }
    return 0;
}
*/