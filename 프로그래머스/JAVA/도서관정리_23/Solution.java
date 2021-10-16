package 도서관정리_23;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution
{
    private final static int CMD_INIT			= 100;
    private final static int CMD_ADD			= 200;
    private final static int CMD_MOVETYPE		= 300;
    private final static int CMD_MOVENAME		= 400;
    private final static int CMD_DELETENAME		= 500;
    private final static int CMD_COUNTBOOK		= 600;

    private final static int MAX_N				= 5;
    private final static int MAX_NAME_LEN		= 7;
    private final static int MAX_TAG_LEN		= 4;

    private final static UserSolution usersolution = new UserSolution();

    private static void String2Char(String s, char[] b)
    {
        int n = s.length();
        for (int i = 0; i < n; ++i)
            b[i] = s.charAt(i);
        b[n] = '\0';
    }

    private static boolean run(BufferedReader br) throws Exception
    {
        int Q;
        int cmd, M, mTypeNum, mSection, mFrom, mTo;

        char mName[]    = new char[MAX_NAME_LEN];
        char mType[]    = new char[MAX_TAG_LEN];
        char mTypes[][] = new char[MAX_N][MAX_TAG_LEN];

        int  ret = 0, ans;

        Q = Integer.parseInt(br.readLine());

        boolean okay = false;

        for (int q = 0; q <= Q; ++q)
        {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");

            cmd = Integer.parseInt(st.nextToken());

            switch(cmd)
            {
                case CMD_INIT:
                    M = Integer.parseInt(st.nextToken());
                    usersolution.init(M);
                    okay = true;
                    break;
                case CMD_ADD:
                    String2Char(st.nextToken(), mName);
                    mTypeNum = Integer.parseInt(st.nextToken());
                    for (int i = 0; i < mTypeNum; ++i)
                        String2Char(st.nextToken(), mTypes[i]);
                    mSection = Integer.parseInt(st.nextToken());
                    if (okay)
                        usersolution.add(mName, mTypeNum, mTypes, mSection);
                    break;
                case CMD_MOVETYPE:
                    String2Char(st.nextToken(), mType);
                    mFrom = Integer.parseInt(st.nextToken());
                    mTo = Integer.parseInt(st.nextToken());
                    if (okay)
                        ret = usersolution.moveType(mType, mFrom, mTo);
                    ans = Integer.parseInt(st.nextToken());
                    if (ret != ans)
                        okay = false;
                    break;
                case CMD_MOVENAME:
                    String2Char(st.nextToken(), mName);
                    mSection = Integer.parseInt(st.nextToken());
                    if (okay)
                        usersolution.moveName(mName, mSection);
                    break;
                case CMD_DELETENAME:
                    String2Char(st.nextToken(), mName);
                    if (okay)
                        usersolution.deleteName(mName);
                    break;
                case CMD_COUNTBOOK:
                    mTypeNum = Integer.parseInt(st.nextToken());
                    for (int i = 0; i < mTypeNum; ++i)
                        String2Char(st.nextToken(), mTypes[i]);
                    mSection = Integer.parseInt(st.nextToken());
                    if (okay)
                        ret = usersolution.countBook(mTypeNum, mTypes, mSection);
                    ans = Integer.parseInt(st.nextToken());
                    if (ret != ans)
                        okay = false;
                    break;
            }
        }

        return okay;
    }

    public static void main(String[] args) throws Exception
    {
        int TC, MARK;

//        System.setIn(new java.io.FileInputStream("res/sample_input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        TC = Integer.parseInt(st.nextToken());
        MARK = Integer.parseInt(st.nextToken());

        for (int testcase = 1; testcase <= TC; ++testcase)
        {
            int score = run(br) ? MARK : 0;

            System.out.println("#" + testcase + " " + score);
        }

        br.close();
    }
}