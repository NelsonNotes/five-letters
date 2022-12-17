import { createAsyncThunk } from '@reduxjs/toolkit'
import { attemptAPI } from '../../api/attempt'
import { TAttemptInput } from '../../types/attempt'

export const make = createAsyncThunk(
	'attempt/makeAttempt',
	async (attempt: TAttemptInput) => {
		return await attemptAPI.postAttempt(attempt)
	}
)
