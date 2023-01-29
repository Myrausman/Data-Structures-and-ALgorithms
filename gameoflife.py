from my2darray import Array2D
class LifeGrid:
    DEAD_CELL=0
    LIVE_CELL=1
    def __init__(self,rows,cols):
        self._grid=Array2D(rows,cols)
        self.configure(list())
    def numRows( self ):
        return self._grid.numRows()
    def numCols( self ):
        return self._grid.numCols()
    def configure( self, coordList ):
        # Clear the game grid.
        for i in range( self.numRows() ):
            for j in range( self.numCols()):
                self.clearCell( i, j )
        for coord in coordList :
            self.setCell( coord[0], coord[1] )

    def isLiveCell( self, row, col ):
        return self._grid[row, col] == self.LIVE_CELL
    def clearCell(self,row,col):
        self._grid[row,col]=self.DEAD_CELL
    def setCell( self, row, col ):
        self._grid[row, col] = self.LIVE_CELL
    def numLiveNeighbors(self,x,y):
        neighbors = 0
        
        

        neighbors += self._grid[x-1][y-1] 
        neighbors += self._grid[x-1][y]   
        neighbors += self._grid[x-1][y+1] 

        neighbors += self._grid[x][y-1]   
        neighbors +=self._grid[x][y+1]   
        neighbors += self._grid[x+1][y-1] 
        neighbors += self._grid[x+1][y]   
        neighbors += self._grid[x+1][y+1] 
                    
        return neighbors


INIT_CONFIG = [ (1,1), (1,2), (2,2), (3,2) ]
GRID_WIDTH = 5
GRID_HEIGHT = 5
NUM_GENS = 8
def main():
    grid = LifeGrid( GRID_WIDTH, GRID_HEIGHT )
    grid.configure( INIT_CONFIG )
    draw( grid )
    for i in range( NUM_GENS ):
        evolve( grid )
        draw( grid )
def evolve(grid):
    LiveCells=list()
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbors=grid.numLiveNeighbors[i,j]
            if (neighbors ==2 and grid.isLiveCell(i,j)) or (neighbors==3):
                LiveCells.append((i,j))
    grid.configure(LiveCells)
def draw(grid):
    for row in range(grid.numRows()):
        for col in range(grid.numCols()):
            if grid.isLiveCell(row, col):
                print ('@',end = " ")
            else:
                print ('.',end = " ")
        print('')
    print('')
main()