import { createAsyncThunk } from '@reduxjs/toolkit'
import { attemptAPI } from '../../api/attempt'
import { userAPI } from '../../api/user'
import { TAttemptInput } from '../../types/attempt'

export const makeAttempt = createAsyncThunk(
	'attempt/makeAttempt',
	async (attempt: TAttemptInput) => {
		return await attemptAPI.postAttempt(attempt)
	}
)
