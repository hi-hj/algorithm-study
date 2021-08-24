package 도서관정리_23;


import java.util.HashMap;
import java.util.HashSet;

class Book{
    String bookName;
    HashSet<char[]> type = new HashSet<char[]>();

    public Book(String bookName, char[][] types){
        this.bookName = bookName;
        for(char[] type : types)
            this.type.add(type);
    }
}

class UserSolution
{
    private final static int MAX_N				= 5;
    private final static int MAX_NAME_LEN		= 7;
    private final static int MAX_TAG_LEN		= 4;

    public static HashMap<Integer, Book> library = new HashMap<Integer, Book>();

    public void init(int M)
    {
        System.out.println(M);
        library.put(0)

    }

    public void add(char mName[], int mTypeNum, char mTypes[][], int mSection)
    {
        library.put(mSection, new Book(mName.toString(), mTypes));
    }

    public int moveType(char mType[], int mFrom, int mTo)
    {
        return 0;
    }

    public void moveName(char mName[], int mSection)
    {

    }

    public void deleteName(char mName[])
    {

    }

    public int countBook(int mTypeNum, char mTypes[][], int mSection)
    {
        return 0;
    }

}
