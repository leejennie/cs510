from page import page
from frame import frame
from dm import diskManager

class BufferPoolFullError(Exception):
	#exception used in the Clock class
	def __init__(self, message):
		self.message = message

class clock:
	def __init__(self):
		# do the required initializations
		self.current = 0

	def pickVictim(self,buffer):
		# find a victim page using the clock algorithm and return the frame number
		# if all pages in the buffer pool are pinned, raise the exception BufferPoolFullError
		
		buf_frame = 0
		victim = 1
		num_buffer = len(buffer)

		# While there is a victim to find
		while(victim == 1):

			try:
				# If the current frame's reference count is 0 and pin count is 0, then it is a victim
				if (buffer[self.current].referenced == 0 and buffer[self.current].pinCount == 0):
					victim = 0
					return self.current

				# If the current frame can be referenced, changed that frame's reference count down by 1 
				elif (buffer[self.current].referenced == 1 and buffer[self.current].pinCount == 0): 
					buffer[self.current].referenced = 0

				self.current = (self.current + 1) % num_buffer 

			except BufferPoolFullError as bu: 
				print(bu)

			# If there are no buffer frames available to be a victim after going through the buffer twice to check
			if (buf_frame > 2 * num_buffer):
				raise BufferPoolFullError('Buffer Pool Full')

			# Move to the next frame
			buf_frame = buf_frame + 1

				
	#implement clock algorithm
#==================================================================================================
		
class bufferManager:
	
	def __init__(self,size):
		self.buffer = []
		self.clk = clock()
		self.dm = diskManager()
		for i in range(size):
			self.buffer.append(frame()) # creating buffer frames (i.e., allocating memory)
			self.buffer[i].frameNumber = i
	#------------------------------------------------------------

	def pin(self, pageNumber, new = False): 
		# given a page number, pin the page in the buffer
		# if new = True, the page is new so no need to read it from disk
		# if new = False, the page already exists. So read it from disk if it is not already in the pool. 

		for i in self.buffer:
			if i.currentPage.pageNo == pageNumber:
				i.pinCount = i.pinCount + 1
				return i.currentPage

		if new == True:
			victim_frame = self.clk.pickVictim(self.buffer)
			if self.buffer[victim_frame].dirtyBit == True:
				self.dm.writePageToDisk(self.buffer[victim_frame].currentPage)
			self.buffer[victim_frame].pinCount = self.buffer[victim_frame].pinCount + 1
			self.buffer[victim_frame].dirtyBit = False
			self.buffer[victim_frame].currentPage.pageNo = pageNumber
			self.buffer[victim_frame].referenced = 1
			return self.buffer[victim_frame].currentPage

		elif new == False:
			victim_frame = self.clk.pickVictim(self.buffer)
			if self.buffer[victim_frame].dirtyBit == True:
					self.dm.writePageToDisk(self.buffer[victim_frame].currentPage)
			self.buffer[victim_frame].currentPage = self.dm.readPageFromDisk(pageNumber)
			self.buffer[victim_frame].pinCount = i.pinCount + 1
			self.buffer[victim_frame].dirtyBit = False
			return self.buffer[victim_frame].currentPage

	#------------------------------------------------------------
	def unpin(self, pageNumber, dirty):
		for i in self.buffer:
			if i.currentPage.pageNo == pageNumber:
				i.pinCount = i.pinCount-1
				i.dirtyBit = i.dirtyBit or dirty	 		

	def flushPage(self,pageNumber): 
		# Ignore this function, it is not needed for this homework.
		# flushPage forces a page in the buffer pool to be written to disk
		for i in range(len(self.buffer)):
			if self.buffer[i].currentPage.pageNo == pageNumber:
				self.dm.writePageToDisk(self.buffer[i].currentPage) # flush writes a page to disk 
				self.buffer[i].dirtyBit = False

	def printBufferContent(self): # helper function to display buffer content on the screen (helpful for debugging)
		print("---------------------------------------------------")
		for i in range(len(self.buffer)):
			print("frame#={} pinCount={} dirtyBit={} referenced={} pageNo={} pageContent={} ".format(self.buffer[i].frameNumber, self.buffer[i].pinCount, self.buffer[i].dirtyBit, self.buffer[i].referenced,  self.buffer[i].currentPage.pageNo, self.buffer[i].currentPage.content))	
		print("---------------------------------------------------")
